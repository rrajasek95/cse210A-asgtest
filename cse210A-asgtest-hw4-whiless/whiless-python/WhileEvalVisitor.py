from WhileVisitor import WhileVisitor

class WhileEvalVisitor(WhileVisitor):
    memory = dict()

    def visitProg(self, ctx):
        return self.visit(ctx.stat())

    def visitLineExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitAdd(self, ctx):
        if ctx.ADD():
            return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))
        else:
            return self.visit(ctx.expr(0)) - self.visit(ctx.expr(1))

    def visitMult(self, ctx):
        if ctx.MUL():
            return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))
        else:
            return self.visit(ctx.expr(0)) / self.visit(ctx.expr(1))

    def visitId(self, ctx):
        return self.memory.get(ctx.ID().getText(), 0)
    
    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitNestExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitAssg(self, ctx):
        self.memory[ctx.ID().getText()] = self.visit(ctx.expr())
        return super().visitAssg(ctx)

    def visitSeq(self, ctx):
        self.visit(ctx.simple_stat())
        self.visit(ctx.stat())

    def visitSingleStat(self, ctx):
        self.visit(ctx.simple_stat())

    def visitIfThenElse(self, ctx):
        if self.visit(ctx.bexpr()):
            self.visit(ctx.simple_stat(0))
        else:
            self.visit(ctx.simple_stat(1))

    def visitWhileDo(self, ctx):
        while self.visit(ctx.bexpr()):
            self.visit(ctx.simple_stat())

    def visitNestStat(self, ctx):
        self.visit(ctx.stat())

    def visitLte(self, ctx):
        return self.visit(ctx.expr(0)) <= self.visit(ctx.expr(1))

    def visitEq(self, ctx):
        return self.visit(ctx.expr(0)) == self.visit(ctx.expr(1))

    def visitLt(self, ctx):
        return self.visit(ctx.expr(0)) < self.visit(ctx.expr(1))

    def visitNot(self, ctx):
        return not self.visit(ctx.bexpr())

    def visitAnd(self, ctx):
        return self.visit(ctx.bexpr(0)) and self.visit(ctx.bexpr(1))
    
    def visitOr(self, ctx):
        return self.visit(ctx.bexpr(0)) or self.visit(ctx.bexpr(1))

    def visitNestBexpr(self, ctx):
        return self.visit(ctx.bexpr())

    def visitTrue(self, ctx):
        return True
    
    def visitFalse(self, ctx):
        return False