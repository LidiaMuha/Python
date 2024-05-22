my_nums = (10, 5, 34, 321, 5, 5)

print(my_nums.count(5))  # 3
print(my_nums.index(5))  # 1
index_1 = my_nums.index(5)  # присваиваем номер индекса переменной
# присваиваем номер индекса второй переменной. Второй аргумент указывает с какого индекса надо начинать поиск
index_2 = my_nums.index(5, index_1 + 1)
print(index_2)
# присваиваем номер индекса третьей переменной
index_3 = my_nums.index(5, index_2 + 1)
print(index_3)


tuple_1 = (False, 'abc', {'user_name': 'Lida'}, 758383)
tuple_2 = ('Hello', [1, 2.5, 43])
tuple_3 = tuple_1 + tuple_2
print(tuple_3)
