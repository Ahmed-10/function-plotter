import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from interpreter import Interpreter
from math_parser import Parser
from lexer import Lexer

class Plot(FigureCanvas):
    def __init__(self, parent, exp, start, stop, step):
        fig, self.ax = plt.subplots(figsize=(8, 5), dpi=80)
        super().__init__(fig)
        self.setParent(parent)

        self.start = start
        self.stop = stop
        self.step = step
        
        self.__evaluate_exp(exp)        
        
        self.ax.set(xlabel='x axis', ylabel='y axis', title=exp)
        self.ax.grid()


    def __evaluate_exp(self, exp):
        lexer = Lexer(exp)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: 
            raise Exception(f"invalid expression: {exp}")
        interpreter = Interpreter(self.start, self.stop, self.step)
        plot_points = interpreter.visit(tree)
        self.range = np.arange(self.start, self.stop, self.step)
        self.ax.plot(self.range, plot_points)