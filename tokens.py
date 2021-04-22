from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    NUM = 0
    VAR = 1
    PLUS = 2
    MINUS = 3
    MULTIPLY = 4
    DIVIDE = 5
    POWER = 6
    LEFT_PARENTHESES = 7
    RIGHT_PARENTHESES = 8


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f": {self.value}" if self.value != None else "")


