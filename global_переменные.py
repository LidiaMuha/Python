c = 5  # глобальная переменная


def my_fn(a, b):
    print(c)
    print(a, b)


my_fn('abc', 'xyz')

# print(a)  # NameError: name 'a' is not defined
# переменная a локальная, она определена внутри функции my_fn
