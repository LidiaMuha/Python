my_num = 0.01

if my_num > 0:
    print(my_num, "- положительное число")
elif my_num < 0:
    print(my_num, "- отрицательное число")
else:
    print("Введённое число является нулём")

print('-----------')


def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        info = "Один из аргументов нецелое число"
    elif a >= b:
        info = f"{a} больше {b}"
    else:
        info = f"{a} меньше {b}"
    return info


print(nums_info(10, True))
print(nums_info(10, 2))
print(nums_info(4, 15))
