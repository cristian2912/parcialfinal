# Generated from Matrices.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MatricesParser import MatricesParser
else:
    from MatricesParser import MatricesParser

# This class defines a complete listener for a parse tree produced by MatricesParser.
class MatricesListener(ParseTreeListener):

    # Enter a parse tree produced by MatricesParser#prog.
    def enterProg(self, ctx:MatricesParser.ProgContext):
        pass

    # Exit a parse tree produced by MatricesParser#prog.
    def exitProg(self, ctx:MatricesParser.ProgContext):
        pass


    # Enter a parse tree produced by MatricesParser#declList.
    def enterDeclList(self, ctx:MatricesParser.DeclListContext):
        pass

    # Exit a parse tree produced by MatricesParser#declList.
    def exitDeclList(self, ctx:MatricesParser.DeclListContext):
        pass


    # Enter a parse tree produced by MatricesParser#decl.
    def enterDecl(self, ctx:MatricesParser.DeclContext):
        pass

    # Exit a parse tree produced by MatricesParser#decl.
    def exitDecl(self, ctx:MatricesParser.DeclContext):
        pass


    # Enter a parse tree produced by MatricesParser#stmtList.
    def enterStmtList(self, ctx:MatricesParser.StmtListContext):
        pass

    # Exit a parse tree produced by MatricesParser#stmtList.
    def exitStmtList(self, ctx:MatricesParser.StmtListContext):
        pass


    # Enter a parse tree produced by MatricesParser#stmt.
    def enterStmt(self, ctx:MatricesParser.StmtContext):
        pass

    # Exit a parse tree produced by MatricesParser#stmt.
    def exitStmt(self, ctx:MatricesParser.StmtContext):
        pass


    # Enter a parse tree produced by MatricesParser#assign.
    def enterAssign(self, ctx:MatricesParser.AssignContext):
        pass

    # Exit a parse tree produced by MatricesParser#assign.
    def exitAssign(self, ctx:MatricesParser.AssignContext):
        pass


    # Enter a parse tree produced by MatricesParser#expr.
    def enterExpr(self, ctx:MatricesParser.ExprContext):
        pass

    # Exit a parse tree produced by MatricesParser#expr.
    def exitExpr(self, ctx:MatricesParser.ExprContext):
        pass


    # Enter a parse tree produced by MatricesParser#term.
    def enterTerm(self, ctx:MatricesParser.TermContext):
        pass

    # Exit a parse tree produced by MatricesParser#term.
    def exitTerm(self, ctx:MatricesParser.TermContext):
        pass


    # Enter a parse tree produced by MatricesParser#factor.
    def enterFactor(self, ctx:MatricesParser.FactorContext):
        pass

    # Exit a parse tree produced by MatricesParser#factor.
    def exitFactor(self, ctx:MatricesParser.FactorContext):
        pass



del MatricesParser