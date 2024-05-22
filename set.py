my_fruits = {'apple', 'banana', 'lime'}
other_fruits = {'banana', 'lime', 'apple'}

print(my_fruits == other_fruits)  # наборы одинаковые
print(id(my_fruits) == id(other_fruits))  # но объекты разные

posts_id = {5, 45989, 5, 24, 32, 5, 32}
print(posts_id)

# print(posts_id[0])  # TypeError: 'set' object is not subscriptable

# У наборов нет метода __getitem__, но набор можно переформатировать в список и использовать
# __getitem__, чтоб получить элемент по его индексу

# list_set = {[1, 2], [6, 3]}  # TypeError: unhashable type: 'list'

list_set = {(1, 2), (6, 3)}
print(list_set)
# del posts_id[1]  # TypeError: 'set' object doesn't support item deletion

new_set = set()  # создание пустого набора, просто вызов пустых скобок {} создасть словать
