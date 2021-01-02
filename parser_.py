# Es parser_.py porque hay un modulo llamado parser

from tokens import TokenType
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def error(self):
        raise Exception("Sintaxis invalida")

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token == None:
            return None
        
        result = self.expr()

        if self.current_token != None:
            self.error()
        
        return result

    def expr(self):
        result = self.term()

        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                AddNode(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                SubtractNode(result, self.term())

        return result

    def term(self):
        result = self.factor()

        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                MultiplyNode(result, self.factor())
            elif self.current_token.type == TokenType.DIVIDE:
                DivideNode(result, self.factor())

        return result

    def factor(self):
        token = self.current_token

        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)

        self.error()