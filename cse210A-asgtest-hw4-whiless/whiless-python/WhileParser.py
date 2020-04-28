# Generated from While.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4*\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\63\n\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\7\5;\n\5\f\5\16\5>\13\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\5\6U\n\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6")
        buf.write("]\n\6\f\6\16\6`\13\6\3\6\2\4\b\n\7\2\4\6\b\n\2\4\3\2\26")
        buf.write("\27\3\2\30\31\2m\2\f\3\2\2\2\4\"\3\2\2\2\6)\3\2\2\2\b")
        buf.write("\62\3\2\2\2\nT\3\2\2\2\f\r\5\6\4\2\r\3\3\2\2\2\16#\7\3")
        buf.write("\2\2\17\20\7\32\2\2\20\21\7\4\2\2\21#\5\b\5\2\22\23\7")
        buf.write("\5\2\2\23\24\5\n\6\2\24\25\7\6\2\2\25\26\5\4\3\2\26\27")
        buf.write("\7\7\2\2\27\30\5\4\3\2\30#\3\2\2\2\31\32\7\b\2\2\32\33")
        buf.write("\5\n\6\2\33\34\7\6\2\2\34\35\5\4\3\2\35#\3\2\2\2\36\37")
        buf.write("\7\t\2\2\37 \5\6\4\2 !\7\n\2\2!#\3\2\2\2\"\16\3\2\2\2")
        buf.write("\"\17\3\2\2\2\"\22\3\2\2\2\"\31\3\2\2\2\"\36\3\2\2\2#")
        buf.write("\5\3\2\2\2$%\5\4\3\2%&\7\13\2\2&\'\5\6\4\2\'*\3\2\2\2")
        buf.write("(*\5\4\3\2)$\3\2\2\2)(\3\2\2\2*\7\3\2\2\2+,\b\5\1\2,\63")
        buf.write("\7\33\2\2-\63\7\32\2\2./\7\f\2\2/\60\5\b\5\2\60\61\7\r")
        buf.write("\2\2\61\63\3\2\2\2\62+\3\2\2\2\62-\3\2\2\2\62.\3\2\2\2")
        buf.write("\63<\3\2\2\2\64\65\f\7\2\2\65\66\t\2\2\2\66;\5\b\5\b\67")
        buf.write("8\f\6\2\289\t\3\2\29;\5\b\5\7:\64\3\2\2\2:\67\3\2\2\2")
        buf.write(";>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\t\3\2\2\2><\3\2\2\2?@")
        buf.write("\b\6\1\2@A\5\b\5\2AB\7\16\2\2BC\5\b\5\2CU\3\2\2\2DE\5")
        buf.write("\b\5\2EF\7\17\2\2FG\5\b\5\2GU\3\2\2\2HI\5\b\5\2IJ\7\20")
        buf.write("\2\2JK\5\b\5\2KU\3\2\2\2LM\7\21\2\2MU\5\n\6\bNU\7\24\2")
        buf.write("\2OU\7\25\2\2PQ\7\f\2\2QR\5\n\6\2RS\7\r\2\2SU\3\2\2\2")
        buf.write("T?\3\2\2\2TD\3\2\2\2TH\3\2\2\2TL\3\2\2\2TN\3\2\2\2TO\3")
        buf.write("\2\2\2TP\3\2\2\2U^\3\2\2\2VW\f\7\2\2WX\7\22\2\2X]\5\n")
        buf.write("\6\bYZ\f\6\2\2Z[\7\23\2\2[]\5\n\6\7\\V\3\2\2\2\\Y\3\2")
        buf.write("\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_\13\3\2\2\2`^\3\2")
        buf.write("\2\2\n\")\62:<T\\^")
        return buf.getvalue()


class WhileParser ( Parser ):

    grammarFileName = "While.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'skip'", "':='", "'if'", "'do'", "'else'", 
                     "'while'", "'{'", "'}'", "';'", "'('", "')'", "'<='", 
                     "'='", "'<'", "'\u00AC'", "'\u2227'", "'\u2228'", "'true'", 
                     "'false'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MUL", "DIV", "ADD", "SUB", "ID", "INT", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_simple_stat = 1
    RULE_stat = 2
    RULE_expr = 3
    RULE_bexpr = 4

    ruleNames =  [ "prog", "simple_stat", "stat", "expr", "bexpr" ]

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
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    MUL=20
    DIV=21
    ADD=22
    SUB=23
    ID=24
    INT=25
    NEWLINE=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self):
            return self.getTypedRuleContext(WhileParser.StatContext,0)


        def getRuleIndex(self):
            return WhileParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = WhileParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.stat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_statContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileParser.RULE_simple_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NestStatContext(Simple_statContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.Simple_statContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stat(self):
            return self.getTypedRuleContext(WhileParser.StatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNestStat" ):
                listener.enterNestStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNestStat" ):
                listener.exitNestStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNestStat" ):
                return visitor.visitNestStat(self)
            else:
                return visitor.visitChildren(self)


    class SkipContext(Simple_statContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.Simple_statContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSkip" ):
                listener.enterSkip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSkip" ):
                listener.exitSkip(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkip" ):
                return visitor.visitSkip(self)
            else:
                return visitor.visitChildren(self)


    class AssgContext(Simple_statContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.Simple_statContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WhileParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(WhileParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssg" ):
                listener.enterAssg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssg" ):
                listener.exitAssg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssg" ):
                return visitor.visitAssg(self)
            else:
                return visitor.visitChildren(self)


    class IfThenElseContext(Simple_statContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.Simple_statContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bexpr(self):
            return self.getTypedRuleContext(WhileParser.BexprContext,0)

        def simple_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.Simple_statContext)
            else:
                return self.getTypedRuleContext(WhileParser.Simple_statContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfThenElse" ):
                listener.enterIfThenElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfThenElse" ):
                listener.exitIfThenElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfThenElse" ):
                return visitor.visitIfThenElse(self)
            else:
                return visitor.visitChildren(self)


    class WhileDoContext(Simple_statContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.Simple_statContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bexpr(self):
            return self.getTypedRuleContext(WhileParser.BexprContext,0)

        def simple_stat(self):
            return self.getTypedRuleContext(WhileParser.Simple_statContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileDo" ):
                listener.enterWhileDo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileDo" ):
                listener.exitWhileDo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileDo" ):
                return visitor.visitWhileDo(self)
            else:
                return visitor.visitChildren(self)



    def simple_stat(self):

        localctx = WhileParser.Simple_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_simple_stat)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WhileParser.T__0]:
                localctx = WhileParser.SkipContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(WhileParser.T__0)
                pass
            elif token in [WhileParser.ID]:
                localctx = WhileParser.AssgContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(WhileParser.ID)
                self.state = 14
                self.match(WhileParser.T__1)
                self.state = 15
                self.expr(0)
                pass
            elif token in [WhileParser.T__2]:
                localctx = WhileParser.IfThenElseContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.match(WhileParser.T__2)
                self.state = 17
                self.bexpr(0)
                self.state = 18
                self.match(WhileParser.T__3)
                self.state = 19
                self.simple_stat()
                self.state = 20
                self.match(WhileParser.T__4)
                self.state = 21
                self.simple_stat()
                pass
            elif token in [WhileParser.T__5]:
                localctx = WhileParser.WhileDoContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 23
                self.match(WhileParser.T__5)
                self.state = 24
                self.bexpr(0)
                self.state = 25
                self.match(WhileParser.T__3)
                self.state = 26
                self.simple_stat()
                pass
            elif token in [WhileParser.T__6]:
                localctx = WhileParser.NestStatContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 28
                self.match(WhileParser.T__6)
                self.state = 29
                self.stat()
                self.state = 30
                self.match(WhileParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SingleStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simple_stat(self):
            return self.getTypedRuleContext(WhileParser.Simple_statContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleStat" ):
                listener.enterSingleStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleStat" ):
                listener.exitSingleStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleStat" ):
                return visitor.visitSingleStat(self)
            else:
                return visitor.visitChildren(self)


    class SeqContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simple_stat(self):
            return self.getTypedRuleContext(WhileParser.Simple_statContext,0)

        def stat(self):
            return self.getTypedRuleContext(WhileParser.StatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeq" ):
                listener.enterSeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeq" ):
                listener.exitSeq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeq" ):
                return visitor.visitSeq(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = WhileParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = WhileParser.SeqContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.simple_stat()
                self.state = 35
                self.match(WhileParser.T__8)
                self.state = 36
                self.stat()
                pass

            elif la_ == 2:
                localctx = WhileParser.SingleStatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.simple_stat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileParser.ExprContext,i)

        def ADD(self):
            return self.getToken(WhileParser.ADD, 0)
        def SUB(self):
            return self.getToken(WhileParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class MultContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileParser.ExprContext,i)

        def MUL(self):
            return self.getToken(WhileParser.MUL, 0)
        def DIV(self):
            return self.getToken(WhileParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMult" ):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WhileParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(WhileParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class NestExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(WhileParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNestExpr" ):
                listener.enterNestExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNestExpr" ):
                listener.exitNestExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNestExpr" ):
                return visitor.visitNestExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WhileParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WhileParser.INT]:
                localctx = WhileParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 42
                self.match(WhileParser.INT)
                pass
            elif token in [WhileParser.ID]:
                localctx = WhileParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(WhileParser.ID)
                pass
            elif token in [WhileParser.T__9]:
                localctx = WhileParser.NestExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(WhileParser.T__9)
                self.state = 45
                self.expr(0)
                self.state = 46
                self.match(WhileParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 56
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = WhileParser.MultContext(self, WhileParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 50
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 51
                        _la = self._input.LA(1)
                        if not(_la==WhileParser.MUL or _la==WhileParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 52
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = WhileParser.AddContext(self, WhileParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 54
                        _la = self._input.LA(1)
                        if not(_la==WhileParser.ADD or _la==WhileParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 55
                        self.expr(5)
                        pass

             
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileParser.RULE_bexpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NotContext(BexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BexprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bexpr(self):
            return self.getTypedRuleContext(WhileParser.BexprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(BexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BexprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.BexprContext)
            else:
                return self.getTypedRuleContext(WhileParser.BexprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(BexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BexprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.BexprContext)
            else:
                return self.getTypedRuleContext(WhileParser.BexprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class LtContext(BexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BexprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLt" ):
                listener.enterLt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLt" ):
                listener.exitLt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLt" ):
                return visitor.visitLt(self)
            else:
                return visitor.visitChildren(self)


    class TrueContext(BexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BexprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrue" ):
                listener.enterTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrue" ):
                listener.exitTrue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrue" ):
                return visitor.visitTrue(self)
            else:
                return visitor.visitChildren(self)


    class FalseContext(BexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BexprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalse" ):
                listener.enterFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalse" ):
                listener.exitFalse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalse" ):
                return visitor.visitFalse(self)
            else:
                return visitor.visitChildren(self)


    class LteContext(BexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BexprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLte" ):
                listener.enterLte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLte" ):
                listener.exitLte(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLte" ):
                return visitor.visitLte(self)
            else:
                return visitor.visitChildren(self)


    class EqContext(BexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BexprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEq" ):
                listener.enterEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEq" ):
                listener.exitEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq" ):
                return visitor.visitEq(self)
            else:
                return visitor.visitChildren(self)


    class NestBexprContext(BexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BexprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bexpr(self):
            return self.getTypedRuleContext(WhileParser.BexprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNestBexpr" ):
                listener.enterNestBexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNestBexpr" ):
                listener.exitNestBexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNestBexpr" ):
                return visitor.visitNestBexpr(self)
            else:
                return visitor.visitChildren(self)



    def bexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WhileParser.BexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_bexpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = WhileParser.LteContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 62
                self.expr(0)
                self.state = 63
                self.match(WhileParser.T__11)
                self.state = 64
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = WhileParser.EqContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self.expr(0)
                self.state = 67
                self.match(WhileParser.T__12)
                self.state = 68
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = WhileParser.LtContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 70
                self.expr(0)
                self.state = 71
                self.match(WhileParser.T__13)
                self.state = 72
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = WhileParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 74
                self.match(WhileParser.T__14)
                self.state = 75
                self.bexpr(6)
                pass

            elif la_ == 5:
                localctx = WhileParser.TrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                self.match(WhileParser.T__17)
                pass

            elif la_ == 6:
                localctx = WhileParser.FalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 77
                self.match(WhileParser.T__18)
                pass

            elif la_ == 7:
                localctx = WhileParser.NestBexprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 78
                self.match(WhileParser.T__9)
                self.state = 79
                self.bexpr(0)
                self.state = 80
                self.match(WhileParser.T__10)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 90
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = WhileParser.AndContext(self, WhileParser.BexprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bexpr)
                        self.state = 84
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 85
                        self.match(WhileParser.T__15)
                        self.state = 86
                        self.bexpr(6)
                        pass

                    elif la_ == 2:
                        localctx = WhileParser.OrContext(self, WhileParser.BexprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bexpr)
                        self.state = 87
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 88
                        self.match(WhileParser.T__16)
                        self.state = 89
                        self.bexpr(5)
                        pass

             
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self._predicates[3] = self.expr_sempred
        self._predicates[4] = self.bexpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

    def bexpr_sempred(self, localctx:BexprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




