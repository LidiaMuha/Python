num_one = 10
num_two = 55

if (num_one > 0 and
    num_two > 0 and
    isinstance(num_one, int) and
        isinstance(num_two, int)):
    print("Введённые числа являются положительными и целыми")

print('--------------')


def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        return "Один из аргументов нецелое число"

    if a >= b:
        return f"{a} больше {b}"

    return f"{a} меньше {b}"


print(nums_info(10, True))
print(nums_info(10, 2))
print(nums_info(4, 15))
