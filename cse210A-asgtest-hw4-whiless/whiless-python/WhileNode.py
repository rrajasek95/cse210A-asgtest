
# Interesting thing to note is that Haskell pattern matching is a form
# of polymorphism, so equivalent approach is to define the 
# same method for different types

class WhileNode(object):
    def __init__(self, type):
        self.type = type

# Arithmetic Expression Nodes
class Expr(WhileNode):
    pass

class Lit(Expr):
    def __init__(self, val):
        super().__init__('LIT')
        self.val = val
    
    def eval(self, memory):
        return self.val

    def show(self):
        return str(self.val)

class Id(Expr):
    def __init__(self, lab):
        super().__init__('ID')
        self.lab = lab
    
    def eval(self, memory):
        return memory.get(self.lab, 0)

    def show(self):
        return self.lab

class Add(Expr):
    def __init__(self, left, right):
        super().__init__('ADD')
        self.left = left
        self.right = right
    
    def eval(self, memory):
        return self.left.eval(memory) + self.right.eval(memory)

    def show(self):
        return "(" + self.left.show() + "+" + self.right.show() + ")"

class Sub(Expr):
    def __init__(self, left, right):
        super().__init__('SUB')
        self.left = left
        self.right = right

    def eval(self, memory):
        return self.left.eval(memory) - self.right.eval(memory)
    
    def show(self):
        return "(" + self.left.show() + "-" + self.right.show() + ")"

class Mul(Expr):
    def __init__(self, left, right):
        super().__init__('MUL')
        self.left = left
        self.right = right

    def eval(self, memory):
        return self.left.eval(memory) * self.right.eval(memory)

    def show(self):
        return "(" + self.left.show() + "*" + self.right.show() + ")"

class Div(Expr):
    def __init__(self, left, right):
        super().__init__('DIV')
        self.left = left
        self.right = right

    def eval(self, memory):
        return self.left.eval(memory) / self.right.eval(memory)

    def show(self):
        return "(" + self.left.show() + "/" + self.right.show() + ")"

# Boolean Expression Nodes

class BExpr(WhileNode):
    pass

class BLit(BExpr):
    def __init__(self, val):
        super().__init__('BLIT')
        self.val = val

    def eval(self, memory):
        return self.val

    def show(self):
        if self.val:
            return "true"
        else:
            return "false"

class LessThanEq(BExpr):
    def __init__(self, e1, e2):
        super().__init__('LTE')
        self.e1 = e1
        self.e2 = e2

    def eval(self, memory):
        return self.e1.eval(memory) <= self.e2.eval(memory)

class Eq(BExpr):
    def __init__(self, e1, e2):
        super().__init__('EQ')
        self.e1 = e1
        self.e2 = e2

    def eval(self, memory):
        return self.e1.eval(memory) == self.e2.eval(memory)
    
    def show(self):
        return "(" + self.e1.show() + "=" + self.e2.show() + ")"
    
class LessThan(BExpr):
    def __init__(self, e1, e2):
        super().__init__('LT')
        self.e1 = e1
        self.e2 = e2

    def eval(self, memory):
        return self.e1.eval(memory) < self.e2.eval(memory)

    def show(self):
        return "(" + self.e1.show() + "<" + self.e2.show() + ")"

class Not(BExpr):
    def __init__(self, b):
        super().__init__('NOT')
        self.b = b

    def eval(self, memory):
        return not self.b.eval(memory)

    def show(self):
        return "¬" + self.b.show()

class And(BExpr):
    def __init__(self, b1, b2):
        super().__init__('AND')
        self.b1 = b1
        self.b2 = b2

    def eval(self, memory):
        return self.b1.eval(memory) and self.b2.eval(memory)

    def show(self):
        return "(" + self.b1.show() + "∧" + self.b2.show() + ")"

class Or(BExpr):
    def __init__(self, b1, b2):
        super().__init__('OR')
        self.b1 = b1
        self.b2 = b2

    def eval(self, memory):
        return self.b1.eval(memory) or self.b2.eval(memory)

    def show(self):
        return "(" + self.b1.show() + "∨" + self.b2.show() + ")"


# Statement Nodes
class Stmt(WhileNode):
    pass

class IfThenElse(Stmt):
    def __init__(self, cond, s1, s2):
        super().__init__('IF')
        self.cond = cond
        self.s1 = s1
        self.s2 = s2

    # Big step variant
    def eval(self, memory):
        if self.cond.eval(memory):
            return self.s1.eval(memory)
        else:
            return self.s2.eval(memory)
    
    # Small step variant
    def evalSS(self, memory):
        if self.cond.eval(memory):
            return (self.s1, memory)
        else:
            return (self.s2, memory)

    def show(self):
        return "if " + self.cond.show() + " then { " + self.s1.show() + " } else { " + self.s2.show() + " }"

class Assign(Stmt):
    def __init__(self, label, expr):
        super().__init__('ASSIGN')
        self.label = label
        self.expr = expr

    def eval(self, memory):
        # Functional style to avoid mutability related bugs
        new_mem = memory.copy()
        new_mem[self.label] = self.expr.eval(memory)
        return new_mem

    # Small step variant
    def evalSS(self, memory):
        new_mem = memory.copy()
        new_mem[self.label] = self.expr.eval(memory)

        return (Skip(), new_mem)

    def show(self):
        return self.label + " := " + self.expr.show()


class Skip(Stmt):
    def __init__(self):
        super().__init__('SKIP')
    
    def eval(self, memory):
        return memory # No-op

    def evalSS(self, memory):
        return (Skip(), memory)

    def show(self):
        return "skip"

class While(Stmt):
    def __init__(self, cond, stmt):
        super().__init__('WHILE')
        self.cond = cond
        self.stmt = stmt

    def eval(self, memory):
        while self.cond.eval(memory):
            # Hope that internal statement doesn't have bugs with memory
            memory = self.stmt.eval(memory)

        return memory

    def evalSS(self, memory):
        if self.cond.eval(memory):
            return (Seq(self.stmt, self), memory)
        else:
            return (Skip(), memory)

    def show(self):
        return "while " + self.cond.show() + " do { " + self.stmt.show() + " }"

class Seq(Stmt):
    def __init__(self, s1, s2):
        super().__init__('SEQ')
        self.s1 = s1
        self.s2 = s2

    def eval(self, memory):
        m1 = self.s1.eval(memory)
        m2 = self.s2.eval(m1)
        return m2

    def evalSS(self, memory):
        if self.s1.type == 'SKIP':
            return (self.s2, memory)
        else:
            (sNew, newMemory) = self.s1.evalSS(memory)
            return (Seq(sNew, self.s2), newMemory)
    
    def show(self):
        return self.s1.show() + "; " + self.s2.show()