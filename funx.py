from antlr4 import *
from funxLexer import funxLexer
from funxParser import funxParser
from visitor import Visitor, VisitorError
from app import create_app
from flask import render_template as render
from flask import redirect, request
from app.forms import InputForm

def start_funx():
    """This function will instantiate the visitor and return it."""
    visitor = Visitor()
    return visitor

visitor = start_funx()  # Start the interpreter
app = create_app()      # Create the flask app
display = []            # This list will be used to store the code and output history

def run_funx(code):
    input_stream = InputStream(code)
    lexer = funxLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = funxParser(token_stream)
    tree = parser.root()
    ret = visitor.visit(tree)
    if ret is not None:
        return ret

@app.route('/', methods=['GET', 'POST'])
def main():
    """
    This is the main page the main page of the interpreter.
    It will be used to recieve the user's input and display the output when run button is clicked.
    When reset button is clicked, the input and output will be cleared.
    The form should be cleared when submit button is clicked.
    """
    input_form = InputForm()
    code = None

    if request.method == 'POST':
        if request.form.get('reset') == 'reset':
            display.clear()
            visitor.reset()
            input_form.input.data = ''
            return redirect('/')
        if request.form.get('clear') == 'clear':
            display.clear()
            input_form.input.data = ''
            return redirect('/')
    # If input_form primary button is clicked, get the input and run it
    if input_form.submit.data and input_form.validate_on_submit():
        code = input_form.input.data
        input_form.input.data = ''
    
    if code is not None:
        display.append({'code': code, 'type': 'input'})
        out = run_funx(code)
        if out is not None:
            if isinstance(out, VisitorError):
                display.append({'code': out.msg, 'type': 'error'})
            else:
                display.append({'code': out, 'type': 'output'})
    
    functions = visitor.func_dict.keys()
    
    context = {
        'input_form': input_form,
        'display': display,
        'functions': functions
    }

    return render('main.html', **context)

@app.route('/report')
def report():
    context = {
    }
    return render('report.html', **context)

app.run(debug=True)
