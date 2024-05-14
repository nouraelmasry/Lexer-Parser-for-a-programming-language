from Variables import *
from Nodes import *
from Token import *
from Error import *

class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None
    
    def register(self, res):
        if isinstance(res, ParseResult):
            if res.error: self.error = res.error
            return res.node
        return res

    def success(self, node):
        self.node = node
        return self        

    def failure(self, error):
        self.error = error
        return self 

class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.nextToken()
    
    def nextToken(self, ):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok
    
    def parse(self):
        res = self.expression()
        if not res.error and self.current_tok.type != EOF:
            return res.failure(InvalidSyntaxError("Expected '+', '-', '*' or '/'"))
        return res
    
    def factor(self):
        res = ParseResult()
        tok = self.current_tok

        if tok.type in (PLUS, MINUS):
            res.register(self.nextToken())
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOpNode(tok, factor))

        elif tok.type in (INT, FLOAT):
            res.register(self.nextToken())
            return res.success(NumberNode(tok))
        
        elif tok.type == LeftPAREN:
            res.register(self.nextToken())
            expr = res.register(self.expression())
            if res.error: return res
            if self.current_tok.type == RightPAREN:
                res.register(self.nextToken())
                return res.success(expr)
            else:
                return res.failure(InvalidSyntaxError("Expected ')'")) 

        return res.failure(InvalidSyntaxError("Expected int or float"))
    

    def term(self):
        return self.bin_op(self.factor, (MULTIPLY, DIV))

    def expression(self):
        return self.bin_op(self.term, (PLUS,MINUS))
    
    def bin_op(self, func, ops):
        res = ParseResult()
        left = res.register(func())
        if res.error: return res

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            res.register(self.nextToken())
            right = res.register(func())
            if res.error: return res

            left = BinOpNode(left, op_tok, right)
        
        return res.success(left)
