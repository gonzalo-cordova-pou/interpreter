# interpreter

# Compile antlr4 grammar
antlr4 -Dlanguage=Python3 -no-listener -visitor Expr.g


# Run flask app
set FLASK_APP=main.py
set FLASK_DEBUG=1
set FLASK_ENV=development
flask run
