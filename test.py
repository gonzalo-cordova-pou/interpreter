from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from TreeVisitor import Visitor, VisitorError

# Welcome message
print(" ________ ___  ___  ________      ___    ___ \n|\\  _____\\\\  \\|\\  \\|\\   ___  \\   |\\  \\  /  /|\n\\ \\  \\__/\\ \\  \\\\\\  \\ \\  \\\\ \\  \\  \\ \\  \\/  / /\n \\ \\   __\\\\ \\  \\\\\\  \\ \\  \\\\ \\  \\  \\ \\    / / \n  \\ \\  \\_| \\ \\  \\\\\\  \\ \\  \\\\ \\  \\  /     \\/  \n   \\ \\__\\   \\ \\_______\\ \\__\\\\ \\__\\/  /\\   \\  \n    \\|__|    \\|_______|\\|__| \\|__/__/ /\\ __\\ \n                                 |__|/ \\|__|")
print("By Gonzalo Cordova\n")
print("Start coding:\n")


visitor = Visitor()
while True:
    input_stream = InputStream(input('? '))
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.root()
    # print(tree.toStringTree(recog=parser))
    ret = visitor.visit(tree)
    if ret is not None:
        if isinstance(ret, VisitorError):
            print(ret.msg)
        else:
            print(ret)
