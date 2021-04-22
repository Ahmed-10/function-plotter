import numpy as np

class Interpreter:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)
    
    def visit_NumberNode(self, node):
        return node.value

    def visit_VariableNode(self, node):
        return np.arange(self.start, self.stop, self.step)

    def visit_str(self, node):
        return np.arange(self.start, self.stop, self.step)

    def visit_AddNode(self, node):
        return self.visit(node.left_node) + self.visit(node.right_node)
    
    def visit_SubtractNode(self, node):
        return self.visit(node.left_node) - self.visit(node.right_node)

    def visit_MultiplyNode(self, node):
        return self.visit(node.left_node) * self.visit(node.right_node)

    def visit_DivideNode(self, node):
        try:
            return self.visit(node.left_node) / self.visit(node.right_node)
        except ZeroDivisionError:
            print("Invalid Math Expression: division by zero")

    def visit_PowerNode(self, node):
        return self.visit(node.left_node) ** self.visit(node.right_node)

    def visit_PlusNode(self, node):
        return self.visit(node.node)

    def visit_MinusNode(self, node):
        return -self.visit(node.node)
