import matplotlib.pyplot as plt
import numpy as np
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
       # print(tree)
       if not tree: continue
       range = np.arange(0.0, 1.0, 0.1)
       interpreter = Interpreter(0.0, 1.0, 0.1)
       value = interpreter.visit(tree)
       print(value)
       fig, ax = plt.subplots()
       ax.plot(range, value)

       ax.set(xlabel='time (s)', ylabel='voltage (mV)',
              title='About as simple as it gets, folks')
       ax.grid()

       fig.savefig("test.png")
       plt.show()