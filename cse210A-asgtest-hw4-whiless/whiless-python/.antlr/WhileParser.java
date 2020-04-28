// Generated from /home/rishi/Documents/UCSC-Courses/CSE210A/HW/cse210A-asgtest/cse210A-asgtest-hw4-whiless/whiless-python/While.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class WhileParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, MUL=20, DIV=21, ADD=22, SUB=23, ID=24, INT=25, NEWLINE=26, 
		WS=27;
	public static final int
		RULE_prog = 0, RULE_simple_stat = 1, RULE_stat = 2, RULE_expr = 3, RULE_bexpr = 4;
	public static final String[] ruleNames = {
		"prog", "simple_stat", "stat", "expr", "bexpr"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'skip'", "':='", "'if'", "'do'", "'else'", "'while'", "'{'", "'}'", 
		"';'", "'('", "')'", "'<='", "'='", "'<'", "'\u00AC'", "'\u2227'", "'\u2228'", 
		"'true'", "'false'", "'*'", "'/'", "'+'", "'-'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, "MUL", "DIV", "ADD", "SUB", 
		"ID", "INT", "NEWLINE", "WS"
	};
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
	public String getGrammarFileName() { return "While.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public WhileParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgContext extends ParserRuleContext {
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10);
			stat();
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

	public static class Simple_statContext extends ParserRuleContext {
		public Simple_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_stat; }
	 
		public Simple_statContext() { }
		public void copyFrom(Simple_statContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class NestStatContext extends Simple_statContext {
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public NestStatContext(Simple_statContext ctx) { copyFrom(ctx); }
	}
	public static class SkipContext extends Simple_statContext {
		public SkipContext(Simple_statContext ctx) { copyFrom(ctx); }
	}
	public static class AssgContext extends Simple_statContext {
		public TerminalNode ID() { return getToken(WhileParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssgContext(Simple_statContext ctx) { copyFrom(ctx); }
	}
	public static class IfThenElseContext extends Simple_statContext {
		public BexprContext bexpr() {
			return getRuleContext(BexprContext.class,0);
		}
		public List<Simple_statContext> simple_stat() {
			return getRuleContexts(Simple_statContext.class);
		}
		public Simple_statContext simple_stat(int i) {
			return getRuleContext(Simple_statContext.class,i);
		}
		public IfThenElseContext(Simple_statContext ctx) { copyFrom(ctx); }
	}
	public static class WhileDoContext extends Simple_statContext {
		public BexprContext bexpr() {
			return getRuleContext(BexprContext.class,0);
		}
		public Simple_statContext simple_stat() {
			return getRuleContext(Simple_statContext.class,0);
		}
		public WhileDoContext(Simple_statContext ctx) { copyFrom(ctx); }
	}

	public final Simple_statContext simple_stat() throws RecognitionException {
		Simple_statContext _localctx = new Simple_statContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_simple_stat);
		try {
			setState(32);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				_localctx = new SkipContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(12);
				match(T__0);
				}
				break;
			case ID:
				_localctx = new AssgContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(13);
				match(ID);
				setState(14);
				match(T__1);
				setState(15);
				expr(0);
				}
				break;
			case T__2:
				_localctx = new IfThenElseContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(16);
				match(T__2);
				setState(17);
				bexpr(0);
				setState(18);
				match(T__3);
				setState(19);
				simple_stat();
				setState(20);
				match(T__4);
				setState(21);
				simple_stat();
				}
				break;
			case T__5:
				_localctx = new WhileDoContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(23);
				match(T__5);
				setState(24);
				bexpr(0);
				setState(25);
				match(T__3);
				setState(26);
				simple_stat();
				}
				break;
			case T__6:
				_localctx = new NestStatContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(28);
				match(T__6);
				setState(29);
				stat();
				setState(30);
				match(T__7);
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class StatContext extends ParserRuleContext {
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	 
		public StatContext() { }
		public void copyFrom(StatContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class SingleStatContext extends StatContext {
		public Simple_statContext simple_stat() {
			return getRuleContext(Simple_statContext.class,0);
		}
		public SingleStatContext(StatContext ctx) { copyFrom(ctx); }
	}
	public static class SeqContext extends StatContext {
		public Simple_statContext simple_stat() {
			return getRuleContext(Simple_statContext.class,0);
		}
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public SeqContext(StatContext ctx) { copyFrom(ctx); }
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_stat);
		try {
			setState(39);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				_localctx = new SeqContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(34);
				simple_stat();
				setState(35);
				match(T__8);
				setState(36);
				stat();
				}
				break;
			case 2:
				_localctx = new SingleStatContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(38);
				simple_stat();
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
	public static class AddContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ADD() { return getToken(WhileParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(WhileParser.SUB, 0); }
		public AddContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class MultContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MUL() { return getToken(WhileParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(WhileParser.DIV, 0); }
		public MultContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class IdContext extends ExprContext {
		public TerminalNode ID() { return getToken(WhileParser.ID, 0); }
		public IdContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class IntContext extends ExprContext {
		public TerminalNode INT() { return getToken(WhileParser.INT, 0); }
		public IntContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class NestExprContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NestExprContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 6;
		enterRecursionRule(_localctx, 6, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				_localctx = new IntContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(42);
				match(INT);
				}
				break;
			case ID:
				{
				_localctx = new IdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(43);
				match(ID);
				}
				break;
			case T__9:
				{
				_localctx = new NestExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(44);
				match(T__9);
				setState(45);
				expr(0);
				setState(46);
				match(T__10);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(58);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(56);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
					case 1:
						{
						_localctx = new MultContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(50);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(51);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(52);
						expr(6);
						}
						break;
					case 2:
						{
						_localctx = new AddContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(53);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(54);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(55);
						expr(5);
						}
						break;
					}
					} 
				}
				setState(60);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
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

	public static class BexprContext extends ParserRuleContext {
		public BexprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bexpr; }
	 
		public BexprContext() { }
		public void copyFrom(BexprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class NotContext extends BexprContext {
		public BexprContext bexpr() {
			return getRuleContext(BexprContext.class,0);
		}
		public NotContext(BexprContext ctx) { copyFrom(ctx); }
	}
	public static class OrContext extends BexprContext {
		public List<BexprContext> bexpr() {
			return getRuleContexts(BexprContext.class);
		}
		public BexprContext bexpr(int i) {
			return getRuleContext(BexprContext.class,i);
		}
		public OrContext(BexprContext ctx) { copyFrom(ctx); }
	}
	public static class AndContext extends BexprContext {
		public List<BexprContext> bexpr() {
			return getRuleContexts(BexprContext.class);
		}
		public BexprContext bexpr(int i) {
			return getRuleContext(BexprContext.class,i);
		}
		public AndContext(BexprContext ctx) { copyFrom(ctx); }
	}
	public static class LtContext extends BexprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public LtContext(BexprContext ctx) { copyFrom(ctx); }
	}
	public static class TrueContext extends BexprContext {
		public TrueContext(BexprContext ctx) { copyFrom(ctx); }
	}
	public static class FalseContext extends BexprContext {
		public FalseContext(BexprContext ctx) { copyFrom(ctx); }
	}
	public static class LteContext extends BexprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public LteContext(BexprContext ctx) { copyFrom(ctx); }
	}
	public static class EqContext extends BexprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public EqContext(BexprContext ctx) { copyFrom(ctx); }
	}
	public static class NestBexprContext extends BexprContext {
		public BexprContext bexpr() {
			return getRuleContext(BexprContext.class,0);
		}
		public NestBexprContext(BexprContext ctx) { copyFrom(ctx); }
	}

	public final BexprContext bexpr() throws RecognitionException {
		return bexpr(0);
	}

	private BexprContext bexpr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		BexprContext _localctx = new BexprContext(_ctx, _parentState);
		BexprContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_bexpr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				_localctx = new LteContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(62);
				expr(0);
				setState(63);
				match(T__11);
				setState(64);
				expr(0);
				}
				break;
			case 2:
				{
				_localctx = new EqContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(66);
				expr(0);
				setState(67);
				match(T__12);
				setState(68);
				expr(0);
				}
				break;
			case 3:
				{
				_localctx = new LtContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(70);
				expr(0);
				setState(71);
				match(T__13);
				setState(72);
				expr(0);
				}
				break;
			case 4:
				{
				_localctx = new NotContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(74);
				match(T__14);
				setState(75);
				bexpr(6);
				}
				break;
			case 5:
				{
				_localctx = new TrueContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(76);
				match(T__17);
				}
				break;
			case 6:
				{
				_localctx = new FalseContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(77);
				match(T__18);
				}
				break;
			case 7:
				{
				_localctx = new NestBexprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(78);
				match(T__9);
				setState(79);
				bexpr(0);
				setState(80);
				match(T__10);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(92);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(90);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
					case 1:
						{
						_localctx = new AndContext(new BexprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_bexpr);
						setState(84);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(85);
						match(T__15);
						setState(86);
						bexpr(6);
						}
						break;
					case 2:
						{
						_localctx = new OrContext(new BexprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_bexpr);
						setState(87);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(88);
						match(T__16);
						setState(89);
						bexpr(5);
						}
						break;
					}
					} 
				}
				setState(94);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
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
		case 3:
			return expr_sempred((ExprContext)_localctx, predIndex);
		case 4:
			return bexpr_sempred((BexprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		}
		return true;
	}
	private boolean bexpr_sempred(BexprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 5);
		case 3:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35b\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\4\3\4\3\4\3\4"+
		"\3\4\5\4*\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\63\n\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\7\5;\n\5\f\5\16\5>\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6U\n\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\7\6]\n\6\f\6\16\6`\13\6\3\6\2\4\b\n\7\2\4\6\b\n\2\4\3\2\26\27"+
		"\3\2\30\31\2m\2\f\3\2\2\2\4\"\3\2\2\2\6)\3\2\2\2\b\62\3\2\2\2\nT\3\2\2"+
		"\2\f\r\5\6\4\2\r\3\3\2\2\2\16#\7\3\2\2\17\20\7\32\2\2\20\21\7\4\2\2\21"+
		"#\5\b\5\2\22\23\7\5\2\2\23\24\5\n\6\2\24\25\7\6\2\2\25\26\5\4\3\2\26\27"+
		"\7\7\2\2\27\30\5\4\3\2\30#\3\2\2\2\31\32\7\b\2\2\32\33\5\n\6\2\33\34\7"+
		"\6\2\2\34\35\5\4\3\2\35#\3\2\2\2\36\37\7\t\2\2\37 \5\6\4\2 !\7\n\2\2!"+
		"#\3\2\2\2\"\16\3\2\2\2\"\17\3\2\2\2\"\22\3\2\2\2\"\31\3\2\2\2\"\36\3\2"+
		"\2\2#\5\3\2\2\2$%\5\4\3\2%&\7\13\2\2&\'\5\6\4\2\'*\3\2\2\2(*\5\4\3\2)"+
		"$\3\2\2\2)(\3\2\2\2*\7\3\2\2\2+,\b\5\1\2,\63\7\33\2\2-\63\7\32\2\2./\7"+
		"\f\2\2/\60\5\b\5\2\60\61\7\r\2\2\61\63\3\2\2\2\62+\3\2\2\2\62-\3\2\2\2"+
		"\62.\3\2\2\2\63<\3\2\2\2\64\65\f\7\2\2\65\66\t\2\2\2\66;\5\b\5\b\678\f"+
		"\6\2\289\t\3\2\29;\5\b\5\7:\64\3\2\2\2:\67\3\2\2\2;>\3\2\2\2<:\3\2\2\2"+
		"<=\3\2\2\2=\t\3\2\2\2><\3\2\2\2?@\b\6\1\2@A\5\b\5\2AB\7\16\2\2BC\5\b\5"+
		"\2CU\3\2\2\2DE\5\b\5\2EF\7\17\2\2FG\5\b\5\2GU\3\2\2\2HI\5\b\5\2IJ\7\20"+
		"\2\2JK\5\b\5\2KU\3\2\2\2LM\7\21\2\2MU\5\n\6\bNU\7\24\2\2OU\7\25\2\2PQ"+
		"\7\f\2\2QR\5\n\6\2RS\7\r\2\2SU\3\2\2\2T?\3\2\2\2TD\3\2\2\2TH\3\2\2\2T"+
		"L\3\2\2\2TN\3\2\2\2TO\3\2\2\2TP\3\2\2\2U^\3\2\2\2VW\f\7\2\2WX\7\22\2\2"+
		"X]\5\n\6\bYZ\f\6\2\2Z[\7\23\2\2[]\5\n\6\7\\V\3\2\2\2\\Y\3\2\2\2]`\3\2"+
		"\2\2^\\\3\2\2\2^_\3\2\2\2_\13\3\2\2\2`^\3\2\2\2\n\")\62:<T\\^";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}