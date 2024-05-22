def mult(a, b):
    return a * b


print(mult(10, 5))

print('-----------------')

# было написано mult = lambda a, b: a * b, и оно заменилось на


def mult_2(a, b): return a * b


print(mult_2(10, 5))
print('-----------------')


def greeting(greet):
    return lambda name: f"{greet}, {name}"


morning_greeting = greeting("Доброе утор")
print(morning_greeting('Лидочка'))


evening_greeting = greeting('Добрый вечер')
print(evening_greeting('Данил'))
