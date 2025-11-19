from enum import Enum


Numeric = int | float

class Operation(Enum):
    ADD = 'add'
    SUBTRACT = 'subtract'
    MULTIPLY = 'multiply'
    DIVIDE = 'divide'

def calculator(a: Numeric, b: Numeric, operation: Operation) -> Numeric:
    match operation:
        case Operation.ADD:
            return a + b
        case Operation.DIVIDE:
            return a / b
        case Operation.MULTIPLY:
            return a * b
        case operation.SUBTRACT:
            return a - b

def is_even(num: Numeric) -> bool:
    return num % 2 == 0


def safe_divide(a: Numeric, b: Numeric) -> Numeric:
    return a / b