def sum(number_1: float, number_2: float) -> float:
    return number_1 + number_2

def subtract(number_1: float, number_2: float) -> float:
    return number_1 - number_2

def multiply(number_1: float, number_2: float) -> float:
    return number_1 * number_2

def divide(number_1: float, number_2: float) -> float:
    if number_2 == 0:
        raise ZeroDivisionError
    return number_1 / number_2
    