// Generated from /home/gonzalo/Documentos/UNI/LP/interpreter/Expr.g by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ExprLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, POW=9, 
		MUL=10, SUM=11, REL=12, LOGIC=13, NOT=14, BOOL=15, ID=16, ID_FUNCTION=17, 
		NUM=18, WS=19;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "POW", 
			"MUL", "SUM", "REL", "LOGIC", "NOT", "BOOL", "ID", "ID_FUNCTION", "NUM", 
			"WS"
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


	public ExprLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Expr.g"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25\u008c\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6"+
		"\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13"+
		"\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\rR\n\r\3\16\3\16\3"+
		"\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16`\n\16\3\17\3\17"+
		"\3\17\3\17\5\17f\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20"+
		"q\n\20\3\21\3\21\7\21u\n\21\f\21\16\21x\13\21\3\22\3\22\7\22|\n\22\f\22"+
		"\16\22\177\13\22\3\23\6\23\u0082\n\23\r\23\16\23\u0083\3\24\6\24\u0087"+
		"\n\24\r\24\16\24\u0088\3\24\3\24\2\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17\t"+
		"\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25\3\2\n\5"+
		"\2\'\',,\61\61\4\2--//\4\2>>@@\3\2c|\6\2\62;C\\aac|\3\2C\\\3\2\62;\4\2"+
		"\f\f\"\"\2\u0099\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13"+
		"\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2"+
		"\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2"+
		"!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2\2\5+\3\2\2\2\7-\3"+
		"\2\2\2\t/\3\2\2\2\13\61\3\2\2\2\r\64\3\2\2\2\17\67\3\2\2\2\21<\3\2\2\2"+
		"\23B\3\2\2\2\25D\3\2\2\2\27F\3\2\2\2\31Q\3\2\2\2\33_\3\2\2\2\35e\3\2\2"+
		"\2\37p\3\2\2\2!r\3\2\2\2#y\3\2\2\2%\u0081\3\2\2\2\'\u0086\3\2\2\2)*\7"+
		"}\2\2*\4\3\2\2\2+,\7\177\2\2,\6\3\2\2\2-.\7*\2\2.\b\3\2\2\2/\60\7+\2\2"+
		"\60\n\3\2\2\2\61\62\7>\2\2\62\63\7/\2\2\63\f\3\2\2\2\64\65\7k\2\2\65\66"+
		"\7h\2\2\66\16\3\2\2\2\678\7g\2\289\7n\2\29:\7u\2\2:;\7g\2\2;\20\3\2\2"+
		"\2<=\7y\2\2=>\7j\2\2>?\7k\2\2?@\7n\2\2@A\7g\2\2A\22\3\2\2\2BC\7`\2\2C"+
		"\24\3\2\2\2DE\t\2\2\2E\26\3\2\2\2FG\t\3\2\2G\30\3\2\2\2HR\t\4\2\2IJ\7"+
		">\2\2JR\7?\2\2KL\7@\2\2LR\7?\2\2MN\7?\2\2NR\7?\2\2OP\7#\2\2PR\7?\2\2Q"+
		"H\3\2\2\2QI\3\2\2\2QK\3\2\2\2QM\3\2\2\2QO\3\2\2\2R\32\3\2\2\2ST\7c\2\2"+
		"TU\7p\2\2U`\7f\2\2VW\7q\2\2W`\7t\2\2XY\7z\2\2YZ\7q\2\2Z`\7t\2\2[\\\7("+
		"\2\2\\`\7(\2\2]^\7~\2\2^`\7~\2\2_S\3\2\2\2_V\3\2\2\2_X\3\2\2\2_[\3\2\2"+
		"\2_]\3\2\2\2`\34\3\2\2\2ab\7p\2\2bc\7q\2\2cf\7v\2\2df\7#\2\2ea\3\2\2\2"+
		"ed\3\2\2\2f\36\3\2\2\2gh\7v\2\2hi\7t\2\2ij\7w\2\2jq\7g\2\2kl\7h\2\2lm"+
		"\7c\2\2mn\7n\2\2no\7u\2\2oq\7g\2\2pg\3\2\2\2pk\3\2\2\2q \3\2\2\2rv\t\5"+
		"\2\2su\t\6\2\2ts\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2\2w\"\3\2\2\2xv\3"+
		"\2\2\2y}\t\7\2\2z|\t\6\2\2{z\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2"+
		"~$\3\2\2\2\177}\3\2\2\2\u0080\u0082\t\b\2\2\u0081\u0080\3\2\2\2\u0082"+
		"\u0083\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084&\3\2\2\2"+
		"\u0085\u0087\t\t\2\2\u0086\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0086"+
		"\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\b\24\2\2"+
		"\u008b(\3\2\2\2\13\2Q_epv}\u0083\u0088\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}