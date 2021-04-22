from tokens import Token, TokenType

WHITE_SPACE = ' /n/t'
DIGITS = '1234567890'
VALID_INPUT = 'x0123456789 /n/t'

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None


    def generate_tokens(self):
        while self.current_char != None: 
            if self.current_char == WHITE_SPACE:
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == 'x':
                self.advance()
                yield Token(TokenType.VAR, 'x')
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '^':
                self.advance()
                yield Token(TokenType.POWER)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LEFT_PARENTHESES)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RIGHT_PARENTHESES)
            elif self.current_char not in VALID_INPUT:
                raise Exception(f"Invalid Input character: {self.current_char}")
            else:
                self.advance()
    

    def generate_number(self):
        decimal_point_counter = 0
        number_str = self.current_char
        self.advance()

        while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_point_counter += 1

            if decimal_point_counter > 1:
                raise Exception(f"Invalid format: numbers can only have one decimal point '{number_str}.'")
            
            number_str += self.current_char
            self.advance()

        if number_str.startswith('.'):
            number_str = '0' + number_str

        if number_str.endswith('.'):
            number_str += '0'

        return Token(TokenType.NUM, float(number_str))
        

            