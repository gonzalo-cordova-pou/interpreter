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
        4,1,21,121,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,3,0,20,8,0,1,0,1,0,1,1,1,1,5,1,26,
        8,1,10,1,12,1,29,9,1,1,1,1,1,1,1,1,1,1,2,4,2,36,8,2,11,2,12,2,37,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,67,8,3,1,4,1,4,1,
        4,5,4,72,8,4,10,4,12,4,75,9,4,1,4,1,4,3,4,79,8,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,114,8,4,
        10,4,12,4,117,9,4,1,5,1,5,1,5,0,1,8,6,0,2,4,6,8,10,0,0,136,0,15,
        1,0,0,0,2,23,1,0,0,0,4,35,1,0,0,0,6,66,1,0,0,0,8,78,1,0,0,0,10,118,
        1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,
        15,16,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,18,20,3,8,4,0,19,18,1,
        0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,
        27,5,8,0,0,24,26,5,7,0,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,
        0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,5,1,0,0,31,32,
        3,4,2,0,32,33,5,2,0,0,33,3,1,0,0,0,34,36,3,6,3,0,35,34,1,0,0,0,36,
        37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,5,1,0,0,0,39,40,5,7,0,
        0,40,41,3,10,5,0,41,42,3,8,4,0,42,67,1,0,0,0,43,67,3,8,4,0,44,45,
        5,3,0,0,45,46,3,8,4,0,46,47,5,1,0,0,47,48,3,4,2,0,48,49,5,2,0,0,
        49,67,1,0,0,0,50,51,5,3,0,0,51,52,3,8,4,0,52,53,5,1,0,0,53,54,3,
        4,2,0,54,55,5,2,0,0,55,56,5,4,0,0,56,57,5,1,0,0,57,58,3,4,2,0,58,
        59,5,2,0,0,59,67,1,0,0,0,60,61,5,5,0,0,61,62,3,8,4,0,62,63,5,1,0,
        0,63,64,3,4,2,0,64,65,5,2,0,0,65,67,1,0,0,0,66,39,1,0,0,0,66,43,
        1,0,0,0,66,44,1,0,0,0,66,50,1,0,0,0,66,60,1,0,0,0,67,7,1,0,0,0,68,
        69,6,4,-1,0,69,73,5,8,0,0,70,72,3,8,4,0,71,70,1,0,0,0,72,75,1,0,
        0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,79,1,0,0,0,75,73,1,0,0,0,76,79,
        5,9,0,0,77,79,5,7,0,0,78,68,1,0,0,0,78,76,1,0,0,0,78,77,1,0,0,0,
        79,115,1,0,0,0,80,81,10,13,0,0,81,82,5,10,0,0,82,114,3,8,4,14,83,
        84,10,12,0,0,84,85,5,11,0,0,85,114,3,8,4,13,86,87,10,11,0,0,87,88,
        5,12,0,0,88,114,3,8,4,12,89,90,10,10,0,0,90,91,5,13,0,0,91,114,3,
        8,4,11,92,93,10,9,0,0,93,94,5,14,0,0,94,114,3,8,4,10,95,96,10,8,
        0,0,96,97,5,15,0,0,97,114,3,8,4,9,98,99,10,7,0,0,99,100,5,16,0,0,
        100,114,3,8,4,7,101,102,10,6,0,0,102,103,5,19,0,0,103,114,3,8,4,
        7,104,105,10,5,0,0,105,106,5,20,0,0,106,114,3,8,4,6,107,108,10,4,
        0,0,108,109,5,17,0,0,109,114,3,8,4,5,110,111,10,3,0,0,111,112,5,
        18,0,0,112,114,3,8,4,4,113,80,1,0,0,0,113,83,1,0,0,0,113,86,1,0,
        0,0,113,89,1,0,0,0,113,92,1,0,0,0,113,95,1,0,0,0,113,98,1,0,0,0,
        113,101,1,0,0,0,113,104,1,0,0,0,113,107,1,0,0,0,113,110,1,0,0,0,
        114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,9,1,0,0,0,117,
        115,1,0,0,0,118,119,5,6,0,0,119,11,1,0,0,0,9,15,19,27,37,66,73,78,
        113,115
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'if'", "'else'", "'while'", 
                     "'<-'", "<INVALID>", "<INVALID>", "<INVALID>", "'='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'^'", "'+'", 
                     "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "ID_FUNCTION", 
                      "NUM", "EQ", "NEQ", "LT", "GT", "LEQ", "GEQ", "POW", 
                      "PLUS", "MINUS", "MUL", "DIV", "WS" ]

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
    ID=7
    ID_FUNCTION=8
    NUM=9
    EQ=10
    NEQ=11
    LT=12
    GT=13
    LEQ=14
    GEQ=15
    POW=16
    PLUS=17
    MINUS=18
    MUL=19
    DIV=20
    WS=21

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
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0:
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
            while _la==7:
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
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 936) != 0):
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
                localctx = ExprParser.AssignationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(ExprParser.ID)
                self.state = 40
                self.assign()
                self.state = 41
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
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
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = ExprParser.FunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 69
                self.match(ExprParser.ID_FUNCTION)
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 70
                        self.expr(0) 
                    self.state = 75
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            elif token in [9]:
                localctx = ExprParser.NumExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                self.match(ExprParser.NUM)
                pass
            elif token in [7]:
                localctx = ExprParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 77
                self.match(ExprParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 113
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.EqualExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 80
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 81
                        self.match(ExprParser.EQ)
                        self.state = 82
                        self.expr(14)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.DifferentExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 83
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 84
                        self.match(ExprParser.NEQ)
                        self.state = 85
                        self.expr(13)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.LessExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 86
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 87
                        self.match(ExprParser.LT)
                        self.state = 88
                        self.expr(12)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.GreaterExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 90
                        self.match(ExprParser.GT)
                        self.state = 91
                        self.expr(11)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.LessEqualExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 92
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 93
                        self.match(ExprParser.LEQ)
                        self.state = 94
                        self.expr(10)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.GreaterEqualExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 95
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 96
                        self.match(ExprParser.GEQ)
                        self.state = 97
                        self.expr(9)
                        pass

                    elif la_ == 7:
                        localctx = ExprParser.PowExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 98
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 99
                        self.match(ExprParser.POW)
                        self.state = 100
                        self.expr(7)
                        pass

                    elif la_ == 8:
                        localctx = ExprParser.MulExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 101
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 102
                        self.match(ExprParser.MUL)
                        self.state = 103
                        self.expr(7)
                        pass

                    elif la_ == 9:
                        localctx = ExprParser.DivExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 104
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 105
                        self.match(ExprParser.DIV)
                        self.state = 106
                        self.expr(6)
                        pass

                    elif la_ == 10:
                        localctx = ExprParser.AddExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 107
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 108
                        self.match(ExprParser.PLUS)
                        self.state = 109
                        self.expr(5)
                        pass

                    elif la_ == 11:
                        localctx = ExprParser.SubExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 111
                        self.match(ExprParser.MINUS)
                        self.state = 112
                        self.expr(4)
                        pass

             
                self.state = 117
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
            self.state = 118
            self.match(ExprParser.T__5)
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
         




