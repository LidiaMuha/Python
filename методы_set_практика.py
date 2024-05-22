my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

# поиск общих элементов наборов
print(my_set.intersection(other_set))
print(other_set.intersection(my_set))

# можно передавать любую(?) последоватьльность, по которой можно проверсти итерацию
print(other_set.intersection('abcd'))
print(other_set & my_set)

print(my_set.union(other_set))
print(my_set | other_set)


# выполняют одно и то же: находят разницу двух множеств
print(my_set.difference(other_set))
print(my_set - other_set)


# удаление элемента из множества
print(my_set.discard('d'))
print(my_set)
# remove работает по-другому: в случае передлачи несуществующего элемента он выдаст ошибку
print(my_set.remove('abc'))
print(my_set)


copied_set = my_set.copy()
copied_set.add('t')
my_set.add('h')
print(copied_set)
print(my_set)

print(my_set.intersection(copied_set))
print(my_set & copied_set)

# элементы, котрых нет в пересечениях
print(my_set.symmetric_difference(copied_set))


# другой способ опредееления элементов вне пересечения
a = {'abc', 'd', 'f', 'y'}
b = {'abc', 'd', 'f', 'l'}

print((a | b) - (a & b))
