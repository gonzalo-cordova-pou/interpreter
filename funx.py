from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from TreeVisitor import Visitor
from app import create_app
from flask import render_template as render
from flask import redirect, request
from app.forms import InputForm

visitor = Visitor()
app = create_app()

input_list = []
output_list = []

def run_funx(code):
    input_stream = InputStream(code)
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.root()
    ret = visitor.visit(tree)
    if ret is not None:
        return ret

@app.route('/', methods=['GET', 'POST'])
def shell():
    """
    This page is the shell for the interpreter.
    It will be used to recieve the user's input and display the output when run button is clicked.
    When reset button is clicked, the input and output will be cleared.
    """
    input_form = InputForm()
    code = None
    
    # If input_form primary button is clicked, get the input and run it
    if input_form.submit.data and input_form.validate_on_submit():
        code = input_form.input.data
    # If input_form reset button is clicked, clear the input and output
    elif input_form.reset.data:
        input_list.clear()
        output_list.clear()
        return redirect('/')
    
    if code is not None:
        input_list.append(code)
        try:
            out = run_funx(code)
            if out is not None:
                output_list.append(out)
        except:
            output_list.append('Error: Invalid input')
    
    context = {
        'input_form': input_form,
        'input_list': input_list,
        'output_list': output_list
    }

    return render('shell.html', **context)

@app.route('/report')
def report():
    context = {
    }
    return render('report.html', **context)

app.run(debug=True)
