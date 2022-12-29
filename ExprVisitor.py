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


    # Visit a parse tree produced by ExprParser#or.
    def visitOr(self, ctx:ExprParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#trueExpr.
    def visitTrueExpr(self, ctx:ExprParser.TrueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lessExpr.
    def visitLessExpr(self, ctx:ExprParser.LessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#subExpr.
    def visitSubExpr(self, ctx:ExprParser.SubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#greaterEqualExpr.
    def visitGreaterEqualExpr(self, ctx:ExprParser.GreaterEqualExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#numExpr.
    def visitNumExpr(self, ctx:ExprParser.NumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#differentExpr.
    def visitDifferentExpr(self, ctx:ExprParser.DifferentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lessEqualExpr.
    def visitLessEqualExpr(self, ctx:ExprParser.LessEqualExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#varExpr.
    def visitVarExpr(self, ctx:ExprParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#greaterExpr.
    def visitGreaterExpr(self, ctx:ExprParser.GreaterExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#not.
    def visitNot(self, ctx:ExprParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addExpr.
    def visitAddExpr(self, ctx:ExprParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parenthesizedExpr.
    def visitParenthesizedExpr(self, ctx:ExprParser.ParenthesizedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#and.
    def visitAnd(self, ctx:ExprParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#functionCall.
    def visitFunctionCall(self, ctx:ExprParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mulExpr.
    def visitMulExpr(self, ctx:ExprParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#divExpr.
    def visitDivExpr(self, ctx:ExprParser.DivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#falseExpr.
    def visitFalseExpr(self, ctx:ExprParser.FalseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#powExpr.
    def visitPowExpr(self, ctx:ExprParser.PowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#equalExpr.
    def visitEqualExpr(self, ctx:ExprParser.EqualExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, ctx:ExprParser.AssignContext):
        return self.visitChildren(ctx)



del ExprParser