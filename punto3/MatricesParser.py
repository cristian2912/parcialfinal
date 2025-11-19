# Generated from Matrices.g4 by ANTLR 4.13.1
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
        4,1,14,83,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,27,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,42,8,3,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,60,
        8,6,10,6,12,6,63,9,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,71,8,7,10,7,12,
        7,74,9,7,1,8,1,8,1,8,1,8,1,8,3,8,81,8,8,1,8,0,2,12,14,9,0,2,4,6,
        8,10,12,14,16,0,0,79,0,18,1,0,0,0,2,26,1,0,0,0,4,28,1,0,0,0,6,41,
        1,0,0,0,8,43,1,0,0,0,10,46,1,0,0,0,12,50,1,0,0,0,14,64,1,0,0,0,16,
        80,1,0,0,0,18,19,3,2,1,0,19,20,3,6,3,0,20,21,5,0,0,1,21,1,1,0,0,
        0,22,23,3,4,2,0,23,24,3,2,1,0,24,27,1,0,0,0,25,27,1,0,0,0,26,22,
        1,0,0,0,26,25,1,0,0,0,27,3,1,0,0,0,28,29,5,1,0,0,29,30,5,2,0,0,30,
        31,5,5,0,0,31,32,5,3,0,0,32,33,5,7,0,0,33,34,5,3,0,0,34,35,5,6,0,
        0,35,36,5,8,0,0,36,5,1,0,0,0,37,38,3,8,4,0,38,39,3,6,3,0,39,42,1,
        0,0,0,40,42,1,0,0,0,41,37,1,0,0,0,41,40,1,0,0,0,42,7,1,0,0,0,43,
        44,3,10,5,0,44,45,5,8,0,0,45,9,1,0,0,0,46,47,5,2,0,0,47,48,5,9,0,
        0,48,49,3,12,6,0,49,11,1,0,0,0,50,51,6,6,-1,0,51,52,3,14,7,0,52,
        61,1,0,0,0,53,54,10,3,0,0,54,55,5,10,0,0,55,60,3,14,7,0,56,57,10,
        2,0,0,57,58,5,11,0,0,58,60,3,14,7,0,59,53,1,0,0,0,59,56,1,0,0,0,
        60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,13,1,0,0,0,63,61,1,
        0,0,0,64,65,6,7,-1,0,65,66,3,16,8,0,66,72,1,0,0,0,67,68,10,2,0,0,
        68,69,5,12,0,0,69,71,3,16,8,0,70,67,1,0,0,0,71,74,1,0,0,0,72,70,
        1,0,0,0,72,73,1,0,0,0,73,15,1,0,0,0,74,72,1,0,0,0,75,81,5,2,0,0,
        76,77,5,13,0,0,77,78,3,12,6,0,78,79,5,14,0,0,79,81,1,0,0,0,80,75,
        1,0,0,0,80,76,1,0,0,0,81,17,1,0,0,0,6,26,41,59,61,72,80
    ]

class MatricesParser ( Parser ):

    grammarFileName = "Matrices.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'mat'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'['", "']'", "','", "';'", "'='", "'+'", "'-'", "'*'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "MAT", "ID", "NUM", "WS", "LBRACK", "RBRACK", 
                      "COMMA", "SEMI", "ASSIGN", "PLUS", "MINUS", "STAR", 
                      "LPAREN", "RPAREN" ]

    RULE_prog = 0
    RULE_declList = 1
    RULE_decl = 2
    RULE_stmtList = 3
    RULE_stmt = 4
    RULE_assign = 5
    RULE_expr = 6
    RULE_term = 7
    RULE_factor = 8

    ruleNames =  [ "prog", "declList", "decl", "stmtList", "stmt", "assign", 
                   "expr", "term", "factor" ]

    EOF = Token.EOF
    MAT=1
    ID=2
    NUM=3
    WS=4
    LBRACK=5
    RBRACK=6
    COMMA=7
    SEMI=8
    ASSIGN=9
    PLUS=10
    MINUS=11
    STAR=12
    LPAREN=13
    RPAREN=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declList(self):
            return self.getTypedRuleContext(MatricesParser.DeclListContext,0)


        def stmtList(self):
            return self.getTypedRuleContext(MatricesParser.StmtListContext,0)


        def EOF(self):
            return self.getToken(MatricesParser.EOF, 0)

        def getRuleIndex(self):
            return MatricesParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = MatricesParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.declList()
            self.state = 19
            self.stmtList()
            self.state = 20
            self.match(MatricesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MatricesParser.DeclContext,0)


        def declList(self):
            return self.getTypedRuleContext(MatricesParser.DeclListContext,0)


        def getRuleIndex(self):
            return MatricesParser.RULE_declList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclList" ):
                listener.enterDeclList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclList" ):
                listener.exitDeclList(self)




    def declList(self):

        localctx = MatricesParser.DeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declList)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.decl()
                self.state = 23
                self.declList()
                pass
            elif token in [-1, 2]:
                self.enterOuterAlt(localctx, 2)

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


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAT(self):
            return self.getToken(MatricesParser.MAT, 0)

        def ID(self):
            return self.getToken(MatricesParser.ID, 0)

        def LBRACK(self):
            return self.getToken(MatricesParser.LBRACK, 0)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(MatricesParser.NUM)
            else:
                return self.getToken(MatricesParser.NUM, i)

        def COMMA(self):
            return self.getToken(MatricesParser.COMMA, 0)

        def RBRACK(self):
            return self.getToken(MatricesParser.RBRACK, 0)

        def SEMI(self):
            return self.getToken(MatricesParser.SEMI, 0)

        def getRuleIndex(self):
            return MatricesParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)




    def decl(self):

        localctx = MatricesParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(MatricesParser.MAT)
            self.state = 29
            self.match(MatricesParser.ID)
            self.state = 30
            self.match(MatricesParser.LBRACK)
            self.state = 31
            self.match(MatricesParser.NUM)
            self.state = 32
            self.match(MatricesParser.COMMA)
            self.state = 33
            self.match(MatricesParser.NUM)
            self.state = 34
            self.match(MatricesParser.RBRACK)
            self.state = 35
            self.match(MatricesParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MatricesParser.StmtContext,0)


        def stmtList(self):
            return self.getTypedRuleContext(MatricesParser.StmtListContext,0)


        def getRuleIndex(self):
            return MatricesParser.RULE_stmtList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtList" ):
                listener.enterStmtList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtList" ):
                listener.exitStmtList(self)




    def stmtList(self):

        localctx = MatricesParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmtList)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.stmt()
                self.state = 38
                self.stmtList()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

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


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(MatricesParser.AssignContext,0)


        def SEMI(self):
            return self.getToken(MatricesParser.SEMI, 0)

        def getRuleIndex(self):
            return MatricesParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = MatricesParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.assign()
            self.state = 44
            self.match(MatricesParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MatricesParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MatricesParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MatricesParser.ExprContext,0)


        def getRuleIndex(self):
            return MatricesParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = MatricesParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(MatricesParser.ID)
            self.state = 47
            self.match(MatricesParser.ASSIGN)
            self.state = 48
            self.expr(0)
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

        def term(self):
            return self.getTypedRuleContext(MatricesParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(MatricesParser.ExprContext,0)


        def PLUS(self):
            return self.getToken(MatricesParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MatricesParser.MINUS, 0)

        def getRuleIndex(self):
            return MatricesParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MatricesParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 59
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = MatricesParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 54
                        self.match(MatricesParser.PLUS)
                        self.state = 55
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = MatricesParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 57
                        self.match(MatricesParser.MINUS)
                        self.state = 58
                        self.term(0)
                        pass

             
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(MatricesParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(MatricesParser.TermContext,0)


        def STAR(self):
            return self.getToken(MatricesParser.STAR, 0)

        def getRuleIndex(self):
            return MatricesParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MatricesParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatricesParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 67
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 68
                    self.match(MatricesParser.STAR)
                    self.state = 69
                    self.factor() 
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MatricesParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MatricesParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MatricesParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MatricesParser.RPAREN, 0)

        def getRuleIndex(self):
            return MatricesParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = MatricesParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_factor)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(MatricesParser.ID)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(MatricesParser.LPAREN)
                self.state = 77
                self.expr(0)
                self.state = 78
                self.match(MatricesParser.RPAREN)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        self._predicates[7] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




