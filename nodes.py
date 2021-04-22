from dataclasses import dataclass

@dataclass
class NumberNode:
    value: any

    def __repr__(self):
        return f"{self.value}"


@dataclass
class AddNode:
    left_node: any
    right_node: any

    def __repr__(self):
        return f"({self.left_node}+{self.right_node})"


@dataclass
class SubtractNode:
    left_node: any
    right_node: any

    def __repr__(self):
        return f"({self.left_node}-{self.right_node})"


@dataclass
class MultiplyNode:
    left_node: any
    right_node: any

    def __repr__(self):
        return f"({self.left_node}*{self.right_node})"


@dataclass
class DivideNode:
    left_node: any
    right_node: any

    def __repr__(self):
        return f"({self.left_node}/{self.right_node})"



@dataclass
class PowerNode:
    left_node: any
    right_node: any

    def __repr__(self):
        return f"({self.left_node}**{self.right_node})"


@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"


@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"