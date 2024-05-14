from Lexer import *
from Parser import *

def execute(text):
    lexer = Lexer(text)
    tokens, error = lexer.makeToken()

    if error: return None, error

    #Generating abstract syntax tree (AST)
    parser = Parser(tokens)
    ast = parser.parse()

    return ast.node, ast.error

