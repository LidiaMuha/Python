my_range = range(7)  # диапазон значений невключая последнее. Напрмер, 7
print(type(my_range))
print(my_range)
print(list(my_range))  # [0, 1, 2, 3, 4, 5, 6]


other_range = range(10, 30, 5)  # диапазон от 10 до 30 (невкл) с шагом 5
print(other_range)
print(list(other_range))

print(other_range[-1])

print('------------------------------')
# проведение итерации
range_2 = range(5)
list_for = []
for n in range_2:
    print(n)

# записала всю последовательность в лист при помощи цикла for
for n in range_2:
    list_for.append(n)

print(list_for)

print('------------------------------')

print(other_range.start)  # ответ 10
print(other_range.stop)  # ответ 30
print(other_range.step)  # ответ 5

print(other_range.index(15))
