# Generated from While.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .WhileParser import WhileParser
else:
    from WhileParser import WhileParser

# This class defines a complete generic visitor for a parse tree produced by WhileParser.

class WhileVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WhileParser#prog.
    def visitProg(self, ctx:WhileParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Skip.
    def visitSkip(self, ctx:WhileParser.SkipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Assg.
    def visitAssg(self, ctx:WhileParser.AssgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#IfThenElse.
    def visitIfThenElse(self, ctx:WhileParser.IfThenElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#WhileDo.
    def visitWhileDo(self, ctx:WhileParser.WhileDoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#NestStat.
    def visitNestStat(self, ctx:WhileParser.NestStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Seq.
    def visitSeq(self, ctx:WhileParser.SeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#SingleStat.
    def visitSingleStat(self, ctx:WhileParser.SingleStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Add.
    def visitAdd(self, ctx:WhileParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Mult.
    def visitMult(self, ctx:WhileParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Id.
    def visitId(self, ctx:WhileParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Int.
    def visitInt(self, ctx:WhileParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#NestExpr.
    def visitNestExpr(self, ctx:WhileParser.NestExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Not.
    def visitNot(self, ctx:WhileParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Or.
    def visitOr(self, ctx:WhileParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#And.
    def visitAnd(self, ctx:WhileParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Lt.
    def visitLt(self, ctx:WhileParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#True.
    def visitTrue(self, ctx:WhileParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#False.
    def visitFalse(self, ctx:WhileParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Lte.
    def visitLte(self, ctx:WhileParser.LteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Eq.
    def visitEq(self, ctx:WhileParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#NestBexpr.
    def visitNestBexpr(self, ctx:WhileParser.NestBexprContext):
        return self.visitChildren(ctx)



del WhileParser