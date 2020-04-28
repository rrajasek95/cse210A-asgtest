from WhileVisitor import WhileVisitor
import WhileNode as wn

import re

class WhileStructVisitor(WhileVisitor):
    def visitProg(self, ctx):
        return self.visit(ctx.stat())
    # Define stmt constructs

    def visitSkip(self, ctx):
        return wn.Skip()
    
    def visitAssg(self, ctx):
        label = ctx.ID().getText()
        expr = self.visit(ctx.expr())
        return wn.Assign(label, expr)

    def visitIfThenElse(self, ctx):
        cond = self.visit(ctx.bexpr())
        s1 = self.visit(ctx.simple_stat(0))
        s2 = self.visit(ctx.simple_stat(1))
        return wn.IfThenElse(cond, s1, s2)

    def visitWhileDo(self, ctx):
        cond = self.visit(ctx.bexpr())
        stmt = self.visit(ctx.simple_stat())
        return wn.While(cond, stmt)

    def visitNestStat(self, ctx):
        return self.visit(ctx.stat())

    def visitSeq(self, ctx):
        s1 = self.visit(ctx.simple_stat())
        s2 = self.visit(ctx.stat())
        return wn.Seq(s1, s2)

    def visitSingleStat(self, ctx):
        return self.visit(ctx.simple_stat())

    # Define expr constructs
    def visitMult(self, ctx):
        e1 = self.visit(ctx.expr(0))
        e2 = self.visit(ctx.expr(1))

        if ctx.MUL():
            return wn.Mul(e1, e2)
        else:
            return wn.Div(e1, e2)

    def visitAdd(self, ctx):
        e1 = self.visit(ctx.expr(0))
        e2 = self.visit(ctx.expr(1))
        if ctx.ADD():
            return wn.Add(e1, e2)
        else:
            return wn.Sub(e1, e2)

    def visitInt(self, ctx):
        val = int(ctx.INT().getText())
        return wn.Lit(val)

    def visitId(self, ctx):
        return wn.Id(ctx.ID().getText())


    def visitNestExpr(self, ctx):
        return self.visit(ctx.expr())

    # Define bexpr constructs
    def visitLte(self, ctx):
        e1 = self.visit(ctx.expr(0))
        e2 = self.visit(ctx.expr(1))
        return wn.LessThanEq(e1, e2)

    def visitLt(self, ctx):
        e1 = self.visit(ctx.expr(0))
        e2 = self.visit(ctx.expr(1))
        return wn.LessThan(e1, e2)

    def visitEq(self, ctx):
        e1 = self.visit(ctx.expr(0))
        e2 = self.visit(ctx.expr(1))
        return wn.Eq(e1, e2)

    def visitNot(self, ctx):
        return wn.Not(self.visit(ctx.bexpr()))
    
    def visitAnd(self, ctx):
        b1 = self.visit(ctx.bexpr(0))
        b2 = self.visit(ctx.bexpr(1))
        return wn.And(b1, b2)

    def visitOr(self, ctx):
        b1 = self.visit(ctx.bexpr(0))
        b2 = self.visit(ctx.bexpr(1))
        return wn.Or(b1, b2)

    def visitNestBexpr(self, ctx):
        return self.visit(ctx.bexpr())

    def visitFalse(self, ctx):
        return wn.BLit(False)

    def visitTrue(self, ctx):
        return wn.BLit(True)