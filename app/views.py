from flask import render_template as render
from .forms import InputForm

def shell():
    """
    This page is the shell for the interpreter.
    It will be used to recieve the user's input and display the output.
    """
    input_form = InputForm()
    context = {
        'input_form': input_form,
    }

    if input_form.validate_on_submit():
        pass

    return render('shell.html', **context)

def report():
    context = {
    }
    
    return render('report.html', **context)