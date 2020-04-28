# Generated from While.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .WhileParser import WhileParser
else:
    from WhileParser import WhileParser

# This class defines a complete listener for a parse tree produced by WhileParser.
class WhileListener(ParseTreeListener):

    # Enter a parse tree produced by WhileParser#prog.
    def enterProg(self, ctx:WhileParser.ProgContext):
        pass

    # Exit a parse tree produced by WhileParser#prog.
    def exitProg(self, ctx:WhileParser.ProgContext):
        pass


    # Enter a parse tree produced by WhileParser#Skip.
    def enterSkip(self, ctx:WhileParser.SkipContext):
        pass

    # Exit a parse tree produced by WhileParser#Skip.
    def exitSkip(self, ctx:WhileParser.SkipContext):
        pass


    # Enter a parse tree produced by WhileParser#Assg.
    def enterAssg(self, ctx:WhileParser.AssgContext):
        pass

    # Exit a parse tree produced by WhileParser#Assg.
    def exitAssg(self, ctx:WhileParser.AssgContext):
        pass


    # Enter a parse tree produced by WhileParser#IfThenElse.
    def enterIfThenElse(self, ctx:WhileParser.IfThenElseContext):
        pass

    # Exit a parse tree produced by WhileParser#IfThenElse.
    def exitIfThenElse(self, ctx:WhileParser.IfThenElseContext):
        pass


    # Enter a parse tree produced by WhileParser#WhileDo.
    def enterWhileDo(self, ctx:WhileParser.WhileDoContext):
        pass

    # Exit a parse tree produced by WhileParser#WhileDo.
    def exitWhileDo(self, ctx:WhileParser.WhileDoContext):
        pass


    # Enter a parse tree produced by WhileParser#NestStat.
    def enterNestStat(self, ctx:WhileParser.NestStatContext):
        pass

    # Exit a parse tree produced by WhileParser#NestStat.
    def exitNestStat(self, ctx:WhileParser.NestStatContext):
        pass


    # Enter a parse tree produced by WhileParser#Seq.
    def enterSeq(self, ctx:WhileParser.SeqContext):
        pass

    # Exit a parse tree produced by WhileParser#Seq.
    def exitSeq(self, ctx:WhileParser.SeqContext):
        pass


    # Enter a parse tree produced by WhileParser#SingleStat.
    def enterSingleStat(self, ctx:WhileParser.SingleStatContext):
        pass

    # Exit a parse tree produced by WhileParser#SingleStat.
    def exitSingleStat(self, ctx:WhileParser.SingleStatContext):
        pass


    # Enter a parse tree produced by WhileParser#Add.
    def enterAdd(self, ctx:WhileParser.AddContext):
        pass

    # Exit a parse tree produced by WhileParser#Add.
    def exitAdd(self, ctx:WhileParser.AddContext):
        pass


    # Enter a parse tree produced by WhileParser#Mult.
    def enterMult(self, ctx:WhileParser.MultContext):
        pass

    # Exit a parse tree produced by WhileParser#Mult.
    def exitMult(self, ctx:WhileParser.MultContext):
        pass


    # Enter a parse tree produced by WhileParser#Id.
    def enterId(self, ctx:WhileParser.IdContext):
        pass

    # Exit a parse tree produced by WhileParser#Id.
    def exitId(self, ctx:WhileParser.IdContext):
        pass


    # Enter a parse tree produced by WhileParser#Int.
    def enterInt(self, ctx:WhileParser.IntContext):
        pass

    # Exit a parse tree produced by WhileParser#Int.
    def exitInt(self, ctx:WhileParser.IntContext):
        pass


    # Enter a parse tree produced by WhileParser#NestExpr.
    def enterNestExpr(self, ctx:WhileParser.NestExprContext):
        pass

    # Exit a parse tree produced by WhileParser#NestExpr.
    def exitNestExpr(self, ctx:WhileParser.NestExprContext):
        pass


    # Enter a parse tree produced by WhileParser#Not.
    def enterNot(self, ctx:WhileParser.NotContext):
        pass

    # Exit a parse tree produced by WhileParser#Not.
    def exitNot(self, ctx:WhileParser.NotContext):
        pass


    # Enter a parse tree produced by WhileParser#Or.
    def enterOr(self, ctx:WhileParser.OrContext):
        pass

    # Exit a parse tree produced by WhileParser#Or.
    def exitOr(self, ctx:WhileParser.OrContext):
        pass


    # Enter a parse tree produced by WhileParser#And.
    def enterAnd(self, ctx:WhileParser.AndContext):
        pass

    # Exit a parse tree produced by WhileParser#And.
    def exitAnd(self, ctx:WhileParser.AndContext):
        pass


    # Enter a parse tree produced by WhileParser#Lt.
    def enterLt(self, ctx:WhileParser.LtContext):
        pass

    # Exit a parse tree produced by WhileParser#Lt.
    def exitLt(self, ctx:WhileParser.LtContext):
        pass


    # Enter a parse tree produced by WhileParser#True.
    def enterTrue(self, ctx:WhileParser.TrueContext):
        pass

    # Exit a parse tree produced by WhileParser#True.
    def exitTrue(self, ctx:WhileParser.TrueContext):
        pass


    # Enter a parse tree produced by WhileParser#False.
    def enterFalse(self, ctx:WhileParser.FalseContext):
        pass

    # Exit a parse tree produced by WhileParser#False.
    def exitFalse(self, ctx:WhileParser.FalseContext):
        pass


    # Enter a parse tree produced by WhileParser#Lte.
    def enterLte(self, ctx:WhileParser.LteContext):
        pass

    # Exit a parse tree produced by WhileParser#Lte.
    def exitLte(self, ctx:WhileParser.LteContext):
        pass


    # Enter a parse tree produced by WhileParser#Eq.
    def enterEq(self, ctx:WhileParser.EqContext):
        pass

    # Exit a parse tree produced by WhileParser#Eq.
    def exitEq(self, ctx:WhileParser.EqContext):
        pass


    # Enter a parse tree produced by WhileParser#NestBexpr.
    def enterNestBexpr(self, ctx:WhileParser.NestBexprContext):
        pass

    # Exit a parse tree produced by WhileParser#NestBexpr.
    def exitNestBexpr(self, ctx:WhileParser.NestBexprContext):
        pass



del WhileParser