# from nodes import *
from values import Number

class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    
    def visit_NumberNode(self, node):
        return Number(node.value)

    # def visit_float(self, num):
    #     return num


    def visit_AddNode(self, node):
        return Number(self.visit(node.left_node).value + self.visit(node.right_node).value)

    
    def visit_SubtractNode(self, node):
        return Number(self.visit(node.left_node).value - self.visit(node.right_node).value)


    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.left_node).value * self.visit(node.right_node).value)


    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.left_node).value / self.visit(node.right_node).value)
        except ZeroDivisionError:
            print("Invalid Math Expression: division by zero")


    def visit_PowerNode(self, node):
        return Number(node.left_node ** self.visit(node.right_node).value)
    

    def visit_PlusNode(self, node):
        return self.visit(node.node)


    def visit_MinusNode(self, node):
        return Number(- self.visit(node.node).value)
