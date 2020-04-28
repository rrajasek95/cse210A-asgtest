from antlr4 import *
from antlr4.InputStream import InputStream

from WhileLexer import WhileLexer
from WhileParser import WhileParser
from WhileStructVisitor import WhileStructVisitor

if __name__ == "__main__":

    lexer = WhileLexer(InputStream(input()))
    token_stream = CommonTokenStream(lexer)
    parser = WhileParser(token_stream)
    while_prog = parser.prog()    
    visitor = WhileStructVisitor()
    program = visitor.visit(while_prog)
    
    memory = {}
    for i in range(10000):
        if program.type == 'SKIP':
            break
        (program, memory) = program.evalSS(memory)
        
        sorted_result = sorted(memory.items(), key=lambda x: x[0])
        formatted_keys = ", ".join([f"{k} → {v}" for k,v in sorted_result])
    
        output = f"{{{formatted_keys}}}"
        print("⇒ " + program.show() + ", " + output)
        
        
    # final_memory = program.eval({})
    