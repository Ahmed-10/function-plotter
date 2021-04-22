from tokens import Token, TokenType
from nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def raise_sytax_error(self):
        raise Exception(f"Invalid syntax: {self.current_token.value}")

    def parse(self):
        if self.current_token == None:
            return None

        result = self.expression()

        if self.current_token != None:
            if self.current_token == TokenType.POWER:
                raise Exception('this case is under development, please redistribute the power over the expression')
            self.raise_sytax_error()

        return result

    def expression(self):
        result = self.term()

        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())

            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.term())

        return result

    def term(self):
        result = self.factor()

        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.factor())

            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.factor())

        return result

    def factor(self):
        token = self.current_token

        if token.type == TokenType.LEFT_PARENTHESES:
            self.advance()
            result = self.expression()

            if self.current_token.type != TokenType.RIGHT_PARENTHESES:
                self.raise_sytax_error()

            self.advance()
            return result

        elif token.type == TokenType.VAR:
            self.advance()
            if self.current_token != None:
                if self.current_token.type == TokenType.POWER:
                    self.advance()
                    return PowerNode(token.value, self.factor())

            return VariableNode(token.value) 

        elif token.type == TokenType.NUM:
            self.advance()

            if self.current_token != None:
                if self.current_token.type == TokenType.POWER:
                    self.advance()
                    return PowerNode(token.value, self.factor())

            return NumberNode(token.value)

        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.factor())

        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.factor())

        self.raise_sytax_error()
