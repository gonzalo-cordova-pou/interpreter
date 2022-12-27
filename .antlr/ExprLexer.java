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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, ID=9, 
		ID_FUNCTION=10, NUM=11, EQ=12, NEQ=13, LT=14, GT=15, LEQ=16, GEQ=17, POW=18, 
		PLUS=19, MINUS=20, MUL=21, DIV=22, WS=23;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "ID", 
			"ID_FUNCTION", "NUM", "EQ", "NEQ", "LT", "GT", "LEQ", "GEQ", "POW", "PLUS", 
			"MINUS", "MUL", "DIV", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'{'", "'}'", "'if'", "'else'", "'while'", "'('", "')'", "'<-'", 
			null, null, null, "'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'^'", 
			"'+'", "'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "ID", "ID_FUNCTION", 
			"NUM", "EQ", "NEQ", "LT", "GT", "LEQ", "GEQ", "POW", "PLUS", "MINUS", 
			"MUL", "DIV", "WS"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31}\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2\3\2\3"+
		"\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7"+
		"\3\b\3\b\3\t\3\t\3\t\3\n\3\n\7\nM\n\n\f\n\16\nP\13\n\3\13\3\13\7\13T\n"+
		"\13\f\13\16\13W\13\13\3\f\6\fZ\n\f\r\f\16\f[\3\r\3\r\3\16\3\16\3\16\3"+
		"\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3"+
		"\25\3\25\3\26\3\26\3\27\3\27\3\30\6\30x\n\30\r\30\16\30y\3\30\3\30\2\2"+
		"\31\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35"+
		"\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\3\2\7\3\2c|\6\2\62;C\\aac|"+
		"\3\2C\\\3\2\62;\4\2\f\f\"\"\2\u0080\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2"+
		"\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23"+
		"\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2"+
		"\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2"+
		"\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\3\61\3\2\2\2\5\63\3\2\2\2\7\65\3"+
		"\2\2\2\t8\3\2\2\2\13=\3\2\2\2\rC\3\2\2\2\17E\3\2\2\2\21G\3\2\2\2\23J\3"+
		"\2\2\2\25Q\3\2\2\2\27Y\3\2\2\2\31]\3\2\2\2\33_\3\2\2\2\35b\3\2\2\2\37"+
		"d\3\2\2\2!f\3\2\2\2#i\3\2\2\2%l\3\2\2\2\'n\3\2\2\2)p\3\2\2\2+r\3\2\2\2"+
		"-t\3\2\2\2/w\3\2\2\2\61\62\7}\2\2\62\4\3\2\2\2\63\64\7\177\2\2\64\6\3"+
		"\2\2\2\65\66\7k\2\2\66\67\7h\2\2\67\b\3\2\2\289\7g\2\29:\7n\2\2:;\7u\2"+
		"\2;<\7g\2\2<\n\3\2\2\2=>\7y\2\2>?\7j\2\2?@\7k\2\2@A\7n\2\2AB\7g\2\2B\f"+
		"\3\2\2\2CD\7*\2\2D\16\3\2\2\2EF\7+\2\2F\20\3\2\2\2GH\7>\2\2HI\7/\2\2I"+
		"\22\3\2\2\2JN\t\2\2\2KM\t\3\2\2LK\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2"+
		"\2O\24\3\2\2\2PN\3\2\2\2QU\t\4\2\2RT\t\3\2\2SR\3\2\2\2TW\3\2\2\2US\3\2"+
		"\2\2UV\3\2\2\2V\26\3\2\2\2WU\3\2\2\2XZ\t\5\2\2YX\3\2\2\2Z[\3\2\2\2[Y\3"+
		"\2\2\2[\\\3\2\2\2\\\30\3\2\2\2]^\7?\2\2^\32\3\2\2\2_`\7#\2\2`a\7?\2\2"+
		"a\34\3\2\2\2bc\7>\2\2c\36\3\2\2\2de\7@\2\2e \3\2\2\2fg\7>\2\2gh\7?\2\2"+
		"h\"\3\2\2\2ij\7@\2\2jk\7?\2\2k$\3\2\2\2lm\7`\2\2m&\3\2\2\2no\7-\2\2o("+
		"\3\2\2\2pq\7/\2\2q*\3\2\2\2rs\7,\2\2s,\3\2\2\2tu\7\61\2\2u.\3\2\2\2vx"+
		"\t\6\2\2wv\3\2\2\2xy\3\2\2\2yw\3\2\2\2yz\3\2\2\2z{\3\2\2\2{|\b\30\2\2"+
		"|\60\3\2\2\2\7\2NU[y\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}