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
        4,1,23,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,3,0,20,8,0,1,0,1,0,1,1,1,1,5,1,26,
        8,1,10,1,12,1,29,9,1,1,1,1,1,1,1,1,1,1,2,4,2,36,8,2,11,2,12,2,37,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,67,8,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,5,4,76,8,4,10,4,12,4,79,9,4,1,4,1,4,3,4,83,8,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,5,4,118,8,4,10,4,12,4,121,9,4,1,5,1,5,1,5,0,1,8,6,0,2,4,6,8,
        10,0,0,141,0,15,1,0,0,0,2,23,1,0,0,0,4,35,1,0,0,0,6,66,1,0,0,0,8,
        82,1,0,0,0,10,122,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,17,1,0,
        0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,18,20,
        3,8,4,0,19,18,1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,22,5,0,0,1,
        22,1,1,0,0,0,23,27,5,10,0,0,24,26,5,9,0,0,25,24,1,0,0,0,26,29,1,
        0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,
        31,5,1,0,0,31,32,3,4,2,0,32,33,5,2,0,0,33,3,1,0,0,0,34,36,3,6,3,
        0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,5,1,
        0,0,0,39,67,3,8,4,0,40,41,5,9,0,0,41,42,3,10,5,0,42,43,3,8,4,0,43,
        67,1,0,0,0,44,45,5,3,0,0,45,46,3,8,4,0,46,47,5,1,0,0,47,48,3,4,2,
        0,48,49,5,2,0,0,49,67,1,0,0,0,50,51,5,3,0,0,51,52,3,8,4,0,52,53,
        5,1,0,0,53,54,3,4,2,0,54,55,5,2,0,0,55,56,5,4,0,0,56,57,5,1,0,0,
        57,58,3,4,2,0,58,59,5,2,0,0,59,67,1,0,0,0,60,61,5,5,0,0,61,62,3,
        8,4,0,62,63,5,1,0,0,63,64,3,4,2,0,64,65,5,2,0,0,65,67,1,0,0,0,66,
        39,1,0,0,0,66,40,1,0,0,0,66,44,1,0,0,0,66,50,1,0,0,0,66,60,1,0,0,
        0,67,7,1,0,0,0,68,69,6,4,-1,0,69,70,5,6,0,0,70,71,3,8,4,0,71,72,
        5,7,0,0,72,83,1,0,0,0,73,77,5,10,0,0,74,76,3,8,4,0,75,74,1,0,0,0,
        76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,83,1,0,0,0,79,77,1,
        0,0,0,80,83,5,11,0,0,81,83,5,9,0,0,82,68,1,0,0,0,82,73,1,0,0,0,82,
        80,1,0,0,0,82,81,1,0,0,0,83,119,1,0,0,0,84,85,10,13,0,0,85,86,5,
        12,0,0,86,118,3,8,4,14,87,88,10,12,0,0,88,89,5,13,0,0,89,118,3,8,
        4,13,90,91,10,11,0,0,91,92,5,14,0,0,92,118,3,8,4,12,93,94,10,10,
        0,0,94,95,5,15,0,0,95,118,3,8,4,11,96,97,10,9,0,0,97,98,5,16,0,0,
        98,118,3,8,4,10,99,100,10,8,0,0,100,101,5,17,0,0,101,118,3,8,4,9,
        102,103,10,7,0,0,103,104,5,18,0,0,104,118,3,8,4,7,105,106,10,6,0,
        0,106,107,5,21,0,0,107,118,3,8,4,7,108,109,10,5,0,0,109,110,5,22,
        0,0,110,118,3,8,4,6,111,112,10,4,0,0,112,113,5,19,0,0,113,118,3,
        8,4,5,114,115,10,3,0,0,115,116,5,20,0,0,116,118,3,8,4,4,117,84,1,
        0,0,0,117,87,1,0,0,0,117,90,1,0,0,0,117,93,1,0,0,0,117,96,1,0,0,
        0,117,99,1,0,0,0,117,102,1,0,0,0,117,105,1,0,0,0,117,108,1,0,0,0,
        117,111,1,0,0,0,117,114,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,
        119,120,1,0,0,0,120,9,1,0,0,0,121,119,1,0,0,0,122,123,5,8,0,0,123,
        11,1,0,0,0,9,15,19,27,37,66,77,82,117,119
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'if'", "'else'", "'while'", 
                     "'('", "')'", "'<-'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'^'", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "ID_FUNCTION", "NUM", "EQ", "NEQ", 
                      "LT", "GT", "LEQ", "GEQ", "POW", "PLUS", "MINUS", 
                      "MUL", "DIV", "WS" ]

    RULE_root = 0
    RULE_declareFunction = 1
    RULE_block = 2
    RULE_instruc = 3
    RULE_expr = 4
    RULE_assign = 5

    ruleNames =  [ "root", "declareFunction", "block", "instruc", "expr", 
                   "assign" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    ID=9
    ID_FUNCTION=10
    NUM=11
    EQ=12
    NEQ=13
    LT=14
    GT=15
    LEQ=16
    GEQ=17
    POW=18
    PLUS=19
    MINUS=20
    MUL=21
    DIV=22
    WS=23

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
            self.state = 15
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 12
                    self.declareFunction() 
                self.state = 17
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 3648) != 0:
                self.state = 18
                self.expr(0)


            self.state = 21
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
            self.state = 23
            self.match(ExprParser.ID_FUNCTION)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 24
                self.match(ExprParser.ID)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(ExprParser.T__0)
            self.state = 31
            self.block()
            self.state = 32
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
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.instruc()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 3688) != 0):
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
        def assign(self):
            return self.getTypedRuleContext(ExprParser.AssignContext,0)

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
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ExprParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.AssignationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(ExprParser.ID)
                self.state = 41
                self.assign()
                self.state = 42
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = ExprParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.match(ExprParser.T__2)
                self.state = 45
                self.expr(0)
                self.state = 46
                self.match(ExprParser.T__0)
                self.state = 47
                self.block()
                self.state = 48
                self.match(ExprParser.T__1)
                pass

            elif la_ == 4:
                localctx = ExprParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.match(ExprParser.T__2)
                self.state = 51
                self.expr(0)
                self.state = 52
                self.match(ExprParser.T__0)
                self.state = 53
                self.block()
                self.state = 54
                self.match(ExprParser.T__1)
                self.state = 55
                self.match(ExprParser.T__3)
                self.state = 56
                self.match(ExprParser.T__0)
                self.state = 57
                self.block()
                self.state = 58
                self.match(ExprParser.T__1)
                pass

            elif la_ == 5:
                localctx = ExprParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.match(ExprParser.T__4)
                self.state = 61
                self.expr(0)
                self.state = 62
                self.match(ExprParser.T__0)
                self.state = 63
                self.block()
                self.state = 64
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


    class LessExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def LT(self):
            return self.getToken(ExprParser.LT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessExpr" ):
                return visitor.visitLessExpr(self)
            else:
                return visitor.visitChildren(self)


    class SubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubExpr" ):
                return visitor.visitSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class GreaterEqualExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def GEQ(self):
            return self.getToken(ExprParser.GEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterEqualExpr" ):
                return visitor.visitGreaterEqualExpr(self)
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


    class DifferentExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def NEQ(self):
            return self.getToken(ExprParser.NEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDifferentExpr" ):
                return visitor.visitDifferentExpr(self)
            else:
                return visitor.visitChildren(self)


    class LessEqualExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def LEQ(self):
            return self.getToken(ExprParser.LEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessEqualExpr" ):
                return visitor.visitLessEqualExpr(self)
            else:
                return visitor.visitChildren(self)


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


    class GreaterExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def GT(self):
            return self.getToken(ExprParser.GT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterExpr" ):
                return visitor.visitGreaterExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
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


    class DivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivExpr" ):
                return visitor.visitDivExpr(self)
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


    class EqualExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualExpr" ):
                return visitor.visitEqualExpr(self)
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
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = ExprParser.ParenthesizedExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 69
                self.match(ExprParser.T__5)
                self.state = 70
                self.expr(0)
                self.state = 71
                self.match(ExprParser.T__6)
                pass
            elif token in [10]:
                localctx = ExprParser.FunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 73
                self.match(ExprParser.ID_FUNCTION)
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 74
                        self.expr(0) 
                    self.state = 79
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            elif token in [11]:
                localctx = ExprParser.NumExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                self.match(ExprParser.NUM)
                pass
            elif token in [9]:
                localctx = ExprParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                self.match(ExprParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 117
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.EqualExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 84
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 85
                        self.match(ExprParser.EQ)
                        self.state = 86
                        self.expr(14)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.DifferentExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 87
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 88
                        self.match(ExprParser.NEQ)
                        self.state = 89
                        self.expr(13)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.LessExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 90
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 91
                        self.match(ExprParser.LT)
                        self.state = 92
                        self.expr(12)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.GreaterExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 93
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 94
                        self.match(ExprParser.GT)
                        self.state = 95
                        self.expr(11)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.LessEqualExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 96
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 97
                        self.match(ExprParser.LEQ)
                        self.state = 98
                        self.expr(10)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.GreaterEqualExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 99
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 100
                        self.match(ExprParser.GEQ)
                        self.state = 101
                        self.expr(9)
                        pass

                    elif la_ == 7:
                        localctx = ExprParser.PowExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 102
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 103
                        self.match(ExprParser.POW)
                        self.state = 104
                        self.expr(7)
                        pass

                    elif la_ == 8:
                        localctx = ExprParser.MulExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 105
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 106
                        self.match(ExprParser.MUL)
                        self.state = 107
                        self.expr(7)
                        pass

                    elif la_ == 9:
                        localctx = ExprParser.DivExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 108
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 109
                        self.match(ExprParser.DIV)
                        self.state = 110
                        self.expr(6)
                        pass

                    elif la_ == 10:
                        localctx = ExprParser.AddExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 111
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 112
                        self.match(ExprParser.PLUS)
                        self.state = 113
                        self.expr(5)
                        pass

                    elif la_ == 11:
                        localctx = ExprParser.SubExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 114
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 115
                        self.match(ExprParser.MINUS)
                        self.state = 116
                        self.expr(4)
                        pass

             
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = ExprParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(ExprParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         




