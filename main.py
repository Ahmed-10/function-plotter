from interpreter import Interpreter
from math_parser import Parser
from lexer import Lexer

while True:
       text = input("calc >  ")
       lexer = Lexer(text)
       tokens = lexer.generate_tokens()
       # print(list(tokens))
       parser = Parser(tokens)
       tree = parser.parse()
       print(tree)
       