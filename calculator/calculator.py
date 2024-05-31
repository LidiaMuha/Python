from typing import Union


# Union[float, int] - типизация/ожидаемые типы данных
def simple_calculator(num_1: Union[float, int], num_2: Union[float, int], operation: str) -> Union[float, int]:
    if operation == "/":
        return num_1 / num_2
    elif operation == "*":
        return num_1 * num_2
    elif operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
