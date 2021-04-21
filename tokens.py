from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    NUM = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    POWER = 5
    LEFT_PARENTHESES = 6
    RIGHT_PARENTHESES = 7


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f": {self.value}" if self.value != None else "")


