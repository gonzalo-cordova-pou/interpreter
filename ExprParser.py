# Generated from Expr.g by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,109,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,
        0,10,0,12,0,15,9,0,1,0,3,0,18,8,0,1,0,1,0,1,1,1,1,5,1,24,8,1,10,
        1,12,1,27,9,1,1,1,1,1,1,1,1,1,1,2,4,2,34,8,2,11,2,12,2,35,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,68,8,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,5,4,77,8,4,10,4,12,4,80,9,4,1,4,1,4,1,4,
        1,4,1,4,3,4,87,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,5,4,104,8,4,10,4,12,4,107,9,4,1,4,0,1,8,5,0,2,4,6,
        8,0,0,123,0,13,1,0,0,0,2,21,1,0,0,0,4,33,1,0,0,0,6,67,1,0,0,0,8,
        86,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,
        0,13,14,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,16,18,3,8,4,0,17,16,
        1,0,0,0,17,18,1,0,0,0,18,19,1,0,0,0,19,20,5,0,0,1,20,1,1,0,0,0,21,
        25,5,17,0,0,22,24,5,16,0,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,
        0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,1,0,0,29,30,
        3,4,2,0,30,31,5,2,0,0,31,3,1,0,0,0,32,34,3,6,3,0,33,32,1,0,0,0,34,
        35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,5,1,0,0,0,37,38,5,3,0,
        0,38,39,3,6,3,0,39,40,5,4,0,0,40,68,1,0,0,0,41,68,3,8,4,0,42,43,
        5,16,0,0,43,44,5,5,0,0,44,68,3,8,4,0,45,46,5,6,0,0,46,47,3,8,4,0,
        47,48,5,1,0,0,48,49,3,4,2,0,49,50,5,2,0,0,50,68,1,0,0,0,51,52,5,
        6,0,0,52,53,3,8,4,0,53,54,5,1,0,0,54,55,3,4,2,0,55,56,5,2,0,0,56,
        57,5,7,0,0,57,58,5,1,0,0,58,59,3,4,2,0,59,60,5,2,0,0,60,68,1,0,0,
        0,61,62,5,8,0,0,62,63,3,8,4,0,63,64,5,1,0,0,64,65,3,4,2,0,65,66,
        5,2,0,0,66,68,1,0,0,0,67,37,1,0,0,0,67,41,1,0,0,0,67,42,1,0,0,0,
        67,45,1,0,0,0,67,51,1,0,0,0,67,61,1,0,0,0,68,7,1,0,0,0,69,70,6,4,
        -1,0,70,71,5,3,0,0,71,72,3,8,4,0,72,73,5,4,0,0,73,87,1,0,0,0,74,
        78,5,17,0,0,75,77,3,8,4,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,
        0,0,78,79,1,0,0,0,79,87,1,0,0,0,80,78,1,0,0,0,81,82,5,9,0,0,82,87,
        3,8,4,4,83,87,5,15,0,0,84,87,5,18,0,0,85,87,5,16,0,0,86,69,1,0,0,
        0,86,74,1,0,0,0,86,81,1,0,0,0,86,83,1,0,0,0,86,84,1,0,0,0,86,85,
        1,0,0,0,87,105,1,0,0,0,88,89,10,9,0,0,89,90,5,10,0,0,90,104,3,8,
        4,9,91,92,10,8,0,0,92,93,5,11,0,0,93,104,3,8,4,9,94,95,10,7,0,0,
        95,96,5,12,0,0,96,104,3,8,4,8,97,98,10,6,0,0,98,99,5,13,0,0,99,104,
        3,8,4,7,100,101,10,5,0,0,101,102,5,14,0,0,102,104,3,8,4,6,103,88,
        1,0,0,0,103,91,1,0,0,0,103,94,1,0,0,0,103,97,1,0,0,0,103,100,1,0,
        0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,9,1,0,0,
        0,107,105,1,0,0,0,9,13,17,25,35,67,78,86,103,105
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'('", "')'", "'<-'", "'if'", 
                     "'else'", "'while'", "'not'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "POW", "MUL", "SUM", "REL", 
                      "LOGIC", "BOOL", "ID", "ID_FUNCTION", "NUM", "WS" ]

    RULE_root = 0
    RULE_declareFunction = 1
    RULE_block = 2
    RULE_instruc = 3
    RULE_expr = 4

    ruleNames =  [ "root", "declareFunction", "block", "instruc", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    POW=10
    MUL=11
    SUM=12
    REL=13
    LOGIC=14
    BOOL=15
    ID=16
    ID_FUNCTION=17
    NUM=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def declareFunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DeclareFunctionContext)
            else:
                return self.getTypedRuleContext(ExprParser.DeclareFunctionContext,i)


        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 10
                    self.declareFunction() 
                self.state = 15
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 492040) != 0:
                self.state = 16
                self.expr(0)


            self.state = 19
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_FUNCTION(self):
            return self.getToken(ExprParser.ID_FUNCTION, 0)

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def getRuleIndex(self):
            return ExprParser.RULE_declareFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclareFunction" ):
                return visitor.visitDeclareFunction(self)
            else:
                return visitor.visitChildren(self)




    def declareFunction(self):

        localctx = ExprParser.DeclareFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declareFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(ExprParser.ID_FUNCTION)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 22
                self.match(ExprParser.ID)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(ExprParser.T__0)
            self.state = 29
            self.block()
            self.state = 30
            self.match(ExprParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.InstrucContext)
            else:
                return self.getTypedRuleContext(ExprParser.InstrucContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ExprParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.instruc()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 492360) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrucContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_instruc

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignationContext(InstrucContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.InstrucContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignation" ):
                return visitor.visitAssignation(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(InstrucContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.InstrucContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesizedInstrucContext(InstrucContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.InstrucContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def instruc(self):
            return self.getTypedRuleContext(ExprParser.InstrucContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesizedInstruc" ):
                return visitor.visitParenthesizedInstruc(self)
            else:
                return visitor.visitChildren(self)


    class WriteContext(InstrucContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.InstrucContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(InstrucContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.InstrucContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class IfElseContext(InstrucContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.InstrucContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BlockContext)
            else:
                return self.getTypedRuleContext(ExprParser.BlockContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)



    def instruc(self):

        localctx = ExprParser.InstrucContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instruc)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ExprParser.ParenthesizedInstrucContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(ExprParser.T__2)
                self.state = 38
                self.instruc()
                self.state = 39
                self.match(ExprParser.T__3)
                pass

            elif la_ == 2:
                localctx = ExprParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = ExprParser.AssignationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.match(ExprParser.ID)
                self.state = 43
                self.match(ExprParser.T__4)
                self.state = 44
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = ExprParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.match(ExprParser.T__5)
                self.state = 46
                self.expr(0)
                self.state = 47
                self.match(ExprParser.T__0)
                self.state = 48
                self.block()
                self.state = 49
                self.match(ExprParser.T__1)
                pass

            elif la_ == 5:
                localctx = ExprParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.match(ExprParser.T__5)
                self.state = 52
                self.expr(0)
                self.state = 53
                self.match(ExprParser.T__0)
                self.state = 54
                self.block()
                self.state = 55
                self.match(ExprParser.T__1)
                self.state = 56
                self.match(ExprParser.T__6)
                self.state = 57
                self.match(ExprParser.T__0)
                self.state = 58
                self.block()
                self.state = 59
                self.match(ExprParser.T__1)
                pass

            elif la_ == 6:
                localctx = ExprParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 61
                self.match(ExprParser.T__7)
                self.state = 62
                self.expr(0)
                self.state = 63
                self.match(ExprParser.T__0)
                self.state = 64
                self.block()
                self.state = 65
                self.match(ExprParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VarExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExpr" ):
                return visitor.visitVarExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class SumExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def SUM(self):
            return self.getToken(ExprParser.SUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumExpr" ):
                return visitor.visitSumExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesizedExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesizedExpr" ):
                return visitor.visitParenthesizedExpr(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_FUNCTION(self):
            return self.getToken(ExprParser.ID_FUNCTION, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class LogicExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def LOGIC(self):
            return self.getToken(ExprParser.LOGIC, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicExpr" ):
                return visitor.visitLogicExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def MUL(self):
            return self.getToken(ExprParser.MUL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class BoolExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(ExprParser.BOOL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)


    class PowExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def POW(self):
            return self.getToken(ExprParser.POW, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowExpr" ):
                return visitor.visitPowExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelationalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def REL(self):
            return self.getToken(ExprParser.REL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumExpr" ):
                return visitor.visitNumExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = ExprParser.ParenthesizedExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 70
                self.match(ExprParser.T__2)
                self.state = 71
                self.expr(0)
                self.state = 72
                self.match(ExprParser.T__3)
                pass
            elif token in [17]:
                localctx = ExprParser.FunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 74
                self.match(ExprParser.ID_FUNCTION)
                self.state = 78
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 75
                        self.expr(0) 
                    self.state = 80
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            elif token in [9]:
                localctx = ExprParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                self.match(ExprParser.T__8)
                self.state = 82
                self.expr(4)
                pass
            elif token in [15]:
                localctx = ExprParser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 83
                self.match(ExprParser.BOOL)
                pass
            elif token in [18]:
                localctx = ExprParser.NumExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84
                self.match(ExprParser.NUM)
                pass
            elif token in [16]:
                localctx = ExprParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 85
                self.match(ExprParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 103
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.PowExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 88
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 89
                        self.match(ExprParser.POW)
                        self.state = 90
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.MulExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 91
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 92
                        self.match(ExprParser.MUL)
                        self.state = 93
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.SumExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 94
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 95
                        self.match(ExprParser.SUM)
                        self.state = 96
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.RelationalExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 97
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 98
                        self.match(ExprParser.REL)
                        self.state = 99
                        self.expr(7)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.LogicExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 100
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 101
                        self.match(ExprParser.LOGIC)
                        self.state = 102
                        self.expr(6)
                        pass

             
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         




