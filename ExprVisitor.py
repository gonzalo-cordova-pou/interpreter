# Generated from Expr.g by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declareFunction.
    def visitDeclareFunction(self, ctx:ExprParser.DeclareFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#block.
    def visitBlock(self, ctx:ExprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parenthesizedInstruc.
    def visitParenthesizedInstruc(self, ctx:ExprParser.ParenthesizedInstrucContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#write.
    def visitWrite(self, ctx:ExprParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignation.
    def visitAssignation(self, ctx:ExprParser.AssignationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#if.
    def visitIf(self, ctx:ExprParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ifElse.
    def visitIfElse(self, ctx:ExprParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#while.
    def visitWhile(self, ctx:ExprParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#varExpr.
    def visitVarExpr(self, ctx:ExprParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#notExpr.
    def visitNotExpr(self, ctx:ExprParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sumExpr.
    def visitSumExpr(self, ctx:ExprParser.SumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parenthesizedExpr.
    def visitParenthesizedExpr(self, ctx:ExprParser.ParenthesizedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#functionCall.
    def visitFunctionCall(self, ctx:ExprParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logicExpr.
    def visitLogicExpr(self, ctx:ExprParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mulExpr.
    def visitMulExpr(self, ctx:ExprParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#boolExpr.
    def visitBoolExpr(self, ctx:ExprParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#powExpr.
    def visitPowExpr(self, ctx:ExprParser.PowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#relationalExpr.
    def visitRelationalExpr(self, ctx:ExprParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#numExpr.
    def visitNumExpr(self, ctx:ExprParser.NumExprContext):
        return self.visitChildren(ctx)



del ExprParser