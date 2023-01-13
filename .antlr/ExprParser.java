// Generated from /home/gonzalo/Documentos/UNI/LP/interpreter/Expr.g by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, POW=9, 
		MUL=10, SUM=11, REL=12, LOGIC=13, NOT=14, BOOL=15, ID=16, ID_FUNCTION=17, 
		NUM=18, WS=19;
	public static final int
		RULE_root = 0, RULE_declareFunction = 1, RULE_block = 2, RULE_instruc = 3, 
		RULE_expr = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "declareFunction", "block", "instruc", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'{'", "'}'", "'('", "')'", "'<-'", "'if'", "'else'", "'while'", 
			"'^'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "POW", "MUL", "SUM", 
			"REL", "LOGIC", "NOT", "BOOL", "ID", "ID_FUNCTION", "NUM", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Expr.g"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class RootContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ExprParser.EOF, 0); }
		public List<DeclareFunctionContext> declareFunction() {
			return getRuleContexts(DeclareFunctionContext.class);
		}
		public DeclareFunctionContext declareFunction(int i) {
			return getRuleContext(DeclareFunctionContext.class,i);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(13);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(10);
					declareFunction();
					}
					} 
				}
				setState(15);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			setState(17);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << NOT) | (1L << BOOL) | (1L << ID) | (1L << ID_FUNCTION) | (1L << NUM))) != 0)) {
				{
				setState(16);
				expr(0);
				}
			}

			setState(19);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclareFunctionContext extends ParserRuleContext {
		public TerminalNode ID_FUNCTION() { return getToken(ExprParser.ID_FUNCTION, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(ExprParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(ExprParser.ID, i);
		}
		public DeclareFunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declareFunction; }
	}

	public final DeclareFunctionContext declareFunction() throws RecognitionException {
		DeclareFunctionContext _localctx = new DeclareFunctionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declareFunction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(21);
			match(ID_FUNCTION);
			setState(25);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(22);
				match(ID);
				}
				}
				setState(27);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(28);
			match(T__0);
			setState(29);
			block();
			setState(30);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public List<InstrucContext> instruc() {
			return getRuleContexts(InstrucContext.class);
		}
		public InstrucContext instruc(int i) {
			return getRuleContext(InstrucContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(32);
				instruc();
				}
				}
				setState(35); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << T__5) | (1L << T__7) | (1L << NOT) | (1L << BOOL) | (1L << ID) | (1L << ID_FUNCTION) | (1L << NUM))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InstrucContext extends ParserRuleContext {
		public InstrucContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruc; }
	 
		public InstrucContext() { }
		public void copyFrom(InstrucContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AssignationContext extends InstrucContext {
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignationContext(InstrucContext ctx) { copyFrom(ctx); }
	}
	public static class WhileContext extends InstrucContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileContext(InstrucContext ctx) { copyFrom(ctx); }
	}
	public static class ParenthesizedInstrucContext extends InstrucContext {
		public InstrucContext instruc() {
			return getRuleContext(InstrucContext.class,0);
		}
		public ParenthesizedInstrucContext(InstrucContext ctx) { copyFrom(ctx); }
	}
	public static class WriteContext extends InstrucContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public WriteContext(InstrucContext ctx) { copyFrom(ctx); }
	}
	public static class IfContext extends InstrucContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public IfContext(InstrucContext ctx) { copyFrom(ctx); }
	}
	public static class IfElseContext extends InstrucContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public IfElseContext(InstrucContext ctx) { copyFrom(ctx); }
	}

	public final InstrucContext instruc() throws RecognitionException {
		InstrucContext _localctx = new InstrucContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_instruc);
		try {
			setState(67);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				_localctx = new ParenthesizedInstrucContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(37);
				match(T__2);
				setState(38);
				instruc();
				setState(39);
				match(T__3);
				}
				break;
			case 2:
				_localctx = new WriteContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(41);
				expr(0);
				}
				break;
			case 3:
				_localctx = new AssignationContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(42);
				match(ID);
				setState(43);
				match(T__4);
				setState(44);
				expr(0);
				}
				break;
			case 4:
				_localctx = new IfContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(45);
				match(T__5);
				setState(46);
				expr(0);
				setState(47);
				match(T__0);
				setState(48);
				block();
				setState(49);
				match(T__1);
				}
				break;
			case 5:
				_localctx = new IfElseContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(51);
				match(T__5);
				setState(52);
				expr(0);
				setState(53);
				match(T__0);
				setState(54);
				block();
				setState(55);
				match(T__1);
				setState(56);
				match(T__6);
				setState(57);
				match(T__0);
				setState(58);
				block();
				setState(59);
				match(T__1);
				}
				break;
			case 6:
				_localctx = new WhileContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(61);
				match(T__7);
				setState(62);
				expr(0);
				setState(63);
				match(T__0);
				setState(64);
				block();
				setState(65);
				match(T__1);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class VarExprContext extends ExprContext {
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public VarExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class NotExprContext extends ExprContext {
		public TerminalNode NOT() { return getToken(ExprParser.NOT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NotExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class SumExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode SUM() { return getToken(ExprParser.SUM, 0); }
		public SumExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ParenthesizedExprContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ParenthesizedExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class FunctionCallContext extends ExprContext {
		public TerminalNode ID_FUNCTION() { return getToken(ExprParser.ID_FUNCTION, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public FunctionCallContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class LogicExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LOGIC() { return getToken(ExprParser.LOGIC, 0); }
		public LogicExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class MulExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MUL() { return getToken(ExprParser.MUL, 0); }
		public MulExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class BoolExprContext extends ExprContext {
		public TerminalNode BOOL() { return getToken(ExprParser.BOOL, 0); }
		public BoolExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class PowExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode POW() { return getToken(ExprParser.POW, 0); }
		public PowExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class RelationalExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode REL() { return getToken(ExprParser.REL, 0); }
		public RelationalExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class NumExprContext extends ExprContext {
		public TerminalNode NUM() { return getToken(ExprParser.NUM, 0); }
		public NumExprContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
				{
				_localctx = new ParenthesizedExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(70);
				match(T__2);
				setState(71);
				expr(0);
				setState(72);
				match(T__3);
				}
				break;
			case ID_FUNCTION:
				{
				_localctx = new FunctionCallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(74);
				match(ID_FUNCTION);
				setState(78);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(75);
						expr(0);
						}
						} 
					}
					setState(80);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				}
				}
				break;
			case NOT:
				{
				_localctx = new NotExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(81);
				match(NOT);
				setState(82);
				expr(4);
				}
				break;
			case BOOL:
				{
				_localctx = new BoolExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(83);
				match(BOOL);
				}
				break;
			case NUM:
				{
				_localctx = new NumExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(84);
				match(NUM);
				}
				break;
			case ID:
				{
				_localctx = new VarExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(85);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(105);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(103);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
					case 1:
						{
						_localctx = new PowExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(88);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(89);
						match(POW);
						setState(90);
						expr(9);
						}
						break;
					case 2:
						{
						_localctx = new MulExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(91);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(92);
						match(MUL);
						setState(93);
						expr(9);
						}
						break;
					case 3:
						{
						_localctx = new SumExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(94);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(95);
						match(SUM);
						setState(96);
						expr(8);
						}
						break;
					case 4:
						{
						_localctx = new RelationalExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(97);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(98);
						match(REL);
						setState(99);
						expr(7);
						}
						break;
					case 5:
						{
						_localctx = new LogicExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(100);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(101);
						match(LOGIC);
						setState(102);
						expr(6);
						}
						break;
					}
					} 
				}
				setState(107);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 9);
		case 1:
			return precpred(_ctx, 8);
		case 2:
			return precpred(_ctx, 7);
		case 3:
			return precpred(_ctx, 6);
		case 4:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25o\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\7\2\16\n\2\f\2\16\2\21\13\2\3\2\5\2\24"+
		"\n\2\3\2\3\2\3\3\3\3\7\3\32\n\3\f\3\16\3\35\13\3\3\3\3\3\3\3\3\3\3\4\6"+
		"\4$\n\4\r\4\16\4%\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5"+
		"\5F\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6O\n\6\f\6\16\6R\13\6\3\6\3\6\3"+
		"\6\3\6\3\6\5\6Y\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\7\6j\n\6\f\6\16\6m\13\6\3\6\2\3\n\7\2\4\6\b\n\2\2\2}\2\17\3"+
		"\2\2\2\4\27\3\2\2\2\6#\3\2\2\2\bE\3\2\2\2\nX\3\2\2\2\f\16\5\4\3\2\r\f"+
		"\3\2\2\2\16\21\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\23\3\2\2\2\21\17"+
		"\3\2\2\2\22\24\5\n\6\2\23\22\3\2\2\2\23\24\3\2\2\2\24\25\3\2\2\2\25\26"+
		"\7\2\2\3\26\3\3\2\2\2\27\33\7\23\2\2\30\32\7\22\2\2\31\30\3\2\2\2\32\35"+
		"\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\36\3\2\2\2\35\33\3\2\2\2\36\37"+
		"\7\3\2\2\37 \5\6\4\2 !\7\4\2\2!\5\3\2\2\2\"$\5\b\5\2#\"\3\2\2\2$%\3\2"+
		"\2\2%#\3\2\2\2%&\3\2\2\2&\7\3\2\2\2\'(\7\5\2\2()\5\b\5\2)*\7\6\2\2*F\3"+
		"\2\2\2+F\5\n\6\2,-\7\22\2\2-.\7\7\2\2.F\5\n\6\2/\60\7\b\2\2\60\61\5\n"+
		"\6\2\61\62\7\3\2\2\62\63\5\6\4\2\63\64\7\4\2\2\64F\3\2\2\2\65\66\7\b\2"+
		"\2\66\67\5\n\6\2\678\7\3\2\289\5\6\4\29:\7\4\2\2:;\7\t\2\2;<\7\3\2\2<"+
		"=\5\6\4\2=>\7\4\2\2>F\3\2\2\2?@\7\n\2\2@A\5\n\6\2AB\7\3\2\2BC\5\6\4\2"+
		"CD\7\4\2\2DF\3\2\2\2E\'\3\2\2\2E+\3\2\2\2E,\3\2\2\2E/\3\2\2\2E\65\3\2"+
		"\2\2E?\3\2\2\2F\t\3\2\2\2GH\b\6\1\2HI\7\5\2\2IJ\5\n\6\2JK\7\6\2\2KY\3"+
		"\2\2\2LP\7\23\2\2MO\5\n\6\2NM\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QY"+
		"\3\2\2\2RP\3\2\2\2ST\7\20\2\2TY\5\n\6\6UY\7\21\2\2VY\7\24\2\2WY\7\22\2"+
		"\2XG\3\2\2\2XL\3\2\2\2XS\3\2\2\2XU\3\2\2\2XV\3\2\2\2XW\3\2\2\2Yk\3\2\2"+
		"\2Z[\f\13\2\2[\\\7\13\2\2\\j\5\n\6\13]^\f\n\2\2^_\7\f\2\2_j\5\n\6\13`"+
		"a\f\t\2\2ab\7\r\2\2bj\5\n\6\ncd\f\b\2\2de\7\16\2\2ej\5\n\6\tfg\f\7\2\2"+
		"gh\7\17\2\2hj\5\n\6\biZ\3\2\2\2i]\3\2\2\2i`\3\2\2\2ic\3\2\2\2if\3\2\2"+
		"\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2l\13\3\2\2\2mk\3\2\2\2\13\17\23\33%EP"+
		"Xik";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}