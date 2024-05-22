try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error - Division by zero!")

print('Continue...')

print('-------------------')

try:
    print(10 / 5)
except ZeroDivisionError as a:
    print(type(a))
    print(a)
except TypeError as a:
    print(a)
else:  # этот блок выполняется в случае успеха
    print("Код выполнен без ошибок")
finally:  # этот блок выполняется всегда
    print('Continue...')


print('-------------------')

try:
    print(10 / 0)
except Exception as e:  # класс Exception - родительский класс оштбок
    print(e)


print('-------------------')

try:
    print(10 / 0)
except:
    print("Какая-то ошибка")
