def divide_nums(a, b):
    if b == 0:
        raise ValueError("Второе число не может быть равно нулю!")
    return a / b


# print(divide_nums(10, 0))

try:
    print(divide_nums(10, 0))
except ValueError as a:
    print(a)
else:  # этот блок выполняется в случае успеха
    print("Код выполнен без ошибок")
finally:  # этот блок выполняется всегда
    print('Continue...')
