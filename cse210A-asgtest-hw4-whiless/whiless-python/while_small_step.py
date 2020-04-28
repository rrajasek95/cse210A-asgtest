from antlr4 import *
from antlr4.InputStream import InputStream

from WhileLexer import WhileLexer
from WhileParser import WhileParser

from WhileEvalVisitor import WhileEvalVisitor

if __name__ == "__main__":

    lexer = WhileLexer(InputStream(input()))
    token_stream = CommonTokenStream(lexer)
    parser = WhileParser(token_stream)
    while_prog = parser.prog()    
    visitor = WhileEvalVisitor()
    visitor.visit(while_prog)
    sorted_result = sorted(visitor.memory.items(), key=lambda x: x[0])
    formatted_keys = ", ".join([f"{k} → {v}" for k,v in sorted_result])
    
    output = f"{{{formatted_keys}}}"
    print(output)