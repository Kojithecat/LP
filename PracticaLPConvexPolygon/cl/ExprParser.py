# Generated from C:/Users/Ra�l/Desktop/Python/Practica/cl\Expr.g4 by ANTLR 4.9
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("[\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\5\2\f\n\2\3\2\3")
        buf.write("\2\3\2\3\2\5\2\22\n\2\3\2\3\2\5\2\26\n\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\7\3*\n\3\f\3\16\3-\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3A\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4N\n")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4V\n\4\f\4\16\4Y\13\4\3\4")
        buf.write("\2\3\6\5\2\4\6\2\2\2l\2\25\3\2\2\2\4@\3\2\2\2\6M\3\2\2")
        buf.write("\2\b\26\7\33\2\2\t\13\5\6\4\2\n\f\7\33\2\2\13\n\3\2\2")
        buf.write("\2\13\f\3\2\2\2\f\r\3\2\2\2\r\16\7\2\2\3\16\26\3\2\2\2")
        buf.write("\17\21\5\4\3\2\20\22\7\33\2\2\21\20\3\2\2\2\21\22\3\2")
        buf.write("\2\2\22\23\3\2\2\2\23\24\7\2\2\3\24\26\3\2\2\2\25\b\3")
        buf.write("\2\2\2\25\t\3\2\2\2\25\17\3\2\2\2\26\3\3\2\2\2\27\30\7")
        buf.write("\21\2\2\30A\5\6\4\2\31\32\7\17\2\2\32A\5\6\4\2\33\34\7")
        buf.write("\16\2\2\34A\5\6\4\2\35\36\7\20\2\2\36A\5\6\4\2\37 \7\23")
        buf.write("\2\2 A\5\6\4\2!\"\7\23\2\2\"A\7\34\2\2#$\7\22\2\2$%\7")
        buf.write("\35\2\2%&\7\3\2\2&+\5\6\4\2\'(\7\3\2\2(*\5\6\4\2)\'\3")
        buf.write("\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,A\3\2\2\2-+\3\2\2")
        buf.write("\2./\7\t\2\2/\60\5\6\4\2\60\61\7\3\2\2\61\62\7\13\2\2")
        buf.write("\62A\3\2\2\2\63\64\7\24\2\2\64\65\5\6\4\2\65\66\7\3\2")
        buf.write("\2\66\67\5\6\4\2\67A\3\2\2\289\7\25\2\29:\5\6\4\2:;\7")
        buf.write("\3\2\2;<\5\6\4\2<A\3\2\2\2=>\7\32\2\2>?\7\4\2\2?A\5\6")
        buf.write("\4\2@\27\3\2\2\2@\31\3\2\2\2@\33\3\2\2\2@\35\3\2\2\2@")
        buf.write("\37\3\2\2\2@!\3\2\2\2@#\3\2\2\2@.\3\2\2\2@\63\3\2\2\2")
        buf.write("@8\3\2\2\2@=\3\2\2\2A\5\3\2\2\2BC\b\4\1\2CD\7\5\2\2DE")
        buf.write("\5\6\4\2EF\7\6\2\2FN\3\2\2\2GN\7\r\2\2HI\7\30\2\2IN\5")
        buf.write("\6\4\5JK\7\31\2\2KN\7\7\2\2LN\7\32\2\2MB\3\2\2\2MG\3\2")
        buf.write("\2\2MH\3\2\2\2MJ\3\2\2\2ML\3\2\2\2NW\3\2\2\2OP\f\7\2\2")
        buf.write("PQ\7\27\2\2QV\5\6\4\bRS\f\6\2\2ST\7\26\2\2TV\5\6\4\7U")
        buf.write("O\3\2\2\2UR\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2X\7\3")
        buf.write("\2\2\2YW\3\2\2\2\n\13\21\25+@MUW")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "', '", "':='", "'('", "')'", "<INVALID>", 
                     "<INVALID>", "'color'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'centroid'", "'vertices'", "'perimeter'", 
                     "'area'", "'draw'", "'print'", "'inside'", "'equal'", 
                     "'+'", "'*'", "'#'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "COORD", "COLOR", "COLCOORD", 
                      "COLORVAL", "POINT", "LISTOFPOINTS", "CENTER", "VERT", 
                      "PERI", "AREA", "DRAW", "PRINT", "INSIDE", "EQUAL", 
                      "UNION", "INTERSEC", "BOUNDINGBOX", "EXCL", "POLYGON", 
                      "COMMENT", "TEXT", "IMGTEXT", "WS" ]

    RULE_root = 0
    RULE_command = 1
    RULE_expr = 2

    ruleNames =  [ "root", "command", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUM=5
    COORD=6
    COLOR=7
    COLCOORD=8
    COLORVAL=9
    POINT=10
    LISTOFPOINTS=11
    CENTER=12
    VERT=13
    PERI=14
    AREA=15
    DRAW=16
    PRINT=17
    INSIDE=18
    EQUAL=19
    UNION=20
    INTERSEC=21
    BOUNDINGBOX=22
    EXCL=23
    POLYGON=24
    COMMENT=25
    TEXT=26
    IMGTEXT=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(ExprParser.COMMENT, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def command(self):
            return self.getTypedRuleContext(ExprParser.CommandContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                var = visitor.visitRoot(self)
                return var
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.match(ExprParser.COMMENT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.expr(0)
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ExprParser.COMMENT:
                    self.state = 8
                    self.match(ExprParser.COMMENT)


                self.state = 11
                self.match(ExprParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 13
                self.command()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ExprParser.COMMENT:
                    self.state = 14
                    self.match(ExprParser.COMMENT)


                self.state = 17
                self.match(ExprParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AREA(self):
            return self.getToken(ExprParser.AREA, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def VERT(self):
            return self.getToken(ExprParser.VERT, 0)

        def CENTER(self):
            return self.getToken(ExprParser.CENTER, 0)

        def PERI(self):
            return self.getToken(ExprParser.PERI, 0)

        def PRINT(self):
            return self.getToken(ExprParser.PRINT, 0)

        def TEXT(self):
            return self.getToken(ExprParser.TEXT, 0)

        def DRAW(self):
            return self.getToken(ExprParser.DRAW, 0)

        def IMGTEXT(self):
            return self.getToken(ExprParser.IMGTEXT, 0)

        def COLOR(self):
            return self.getToken(ExprParser.COLOR, 0)

        def COLORVAL(self):
            return self.getToken(ExprParser.COLORVAL, 0)

        def INSIDE(self):
            return self.getToken(ExprParser.INSIDE, 0)

        def EQUAL(self):
            return self.getToken(ExprParser.EQUAL, 0)

        def POLYGON(self):
            return self.getToken(ExprParser.POLYGON, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                var = visitor.visitCommand(self)
                return var
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = ExprParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(ExprParser.AREA)
                self.state = 22
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(ExprParser.VERT)
                self.state = 24
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(ExprParser.CENTER)
                self.state = 26
                self.expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 27
                self.match(ExprParser.PERI)
                self.state = 28
                self.expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 29
                self.match(ExprParser.PRINT)
                self.state = 30
                self.expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 31
                self.match(ExprParser.PRINT)
                self.state = 32
                self.match(ExprParser.TEXT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 33
                self.match(ExprParser.DRAW)
                self.state = 34
                self.match(ExprParser.IMGTEXT)

                self.state = 35
                self.match(ExprParser.T__0)
                self.state = 36
                self.expr(0)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ExprParser.T__0:
                    self.state = 37
                    self.match(ExprParser.T__0)
                    self.state = 38
                    self.expr(0)
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 44
                self.match(ExprParser.COLOR)
                self.state = 45
                self.expr(0)

                self.state = 46
                self.match(ExprParser.T__0)
                self.state = 47
                self.match(ExprParser.COLORVAL)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 49
                self.match(ExprParser.INSIDE)
                self.state = 50
                self.expr(0)

                self.state = 51
                self.match(ExprParser.T__0)
                self.state = 52
                self.expr(0)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 54
                self.match(ExprParser.EQUAL)
                self.state = 55
                self.expr(0)

                self.state = 56
                self.match(ExprParser.T__0)
                self.state = 57
                self.expr(0)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 59
                self.match(ExprParser.POLYGON)

                self.state = 60
                self.match(ExprParser.T__1)
                self.state = 61
                self.expr(0)
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def LISTOFPOINTS(self):
            return self.getToken(ExprParser.LISTOFPOINTS, 0)

        def BOUNDINGBOX(self):
            return self.getToken(ExprParser.BOUNDINGBOX, 0)

        def EXCL(self):
            return self.getToken(ExprParser.EXCL, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def POLYGON(self):
            return self.getToken(ExprParser.POLYGON, 0)

        def INTERSEC(self):
            return self.getToken(ExprParser.INTERSEC, 0)

        def UNION(self):
            return self.getToken(ExprParser.UNION, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.T__2]:
                self.state = 65
                self.match(ExprParser.T__2)
                self.state = 66
                self.expr(0)
                self.state = 67
                self.match(ExprParser.T__3)
                pass
            elif token in [ExprParser.LISTOFPOINTS]:
                self.state = 69
                self.match(ExprParser.LISTOFPOINTS)
                pass
            elif token in [ExprParser.BOUNDINGBOX]:
                self.state = 70
                self.match(ExprParser.BOUNDINGBOX)
                self.state = 71
                self.expr(3)
                pass
            elif token in [ExprParser.EXCL]:
                self.state = 72
                self.match(ExprParser.EXCL)
                self.state = 73
                self.match(ExprParser.NUM)
                pass
            elif token in [ExprParser.POLYGON]:
                self.state = 74
                self.match(ExprParser.POLYGON)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 83
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 77
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 78
                        self.match(ExprParser.INTERSEC)
                        self.state = 79
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 80
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 81
                        self.match(ExprParser.UNION)
                        self.state = 82
                        self.expr(5)
                        pass

             
                self.state = 87
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
        self._predicates[2] = self.expr_sempred
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
         




