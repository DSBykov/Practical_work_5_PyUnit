from enum import Enum


class Operation(Enum):
    ADD = 'add'
    SUBTRACT = 'subtract'
    MULTIPLY = 'multiply'
    DIVIDE = 'divide'

def calculator(a: float | int, b: float | int, operation: Operation) -> int | float:
    match operation:
        case Operation.ADD:
            return a + b
        case Operation.DIVIDE:
            return a / b
        case Operation.MULTIPLY:
            return a * b
        case operation.SUBTRACT:
            return a - b