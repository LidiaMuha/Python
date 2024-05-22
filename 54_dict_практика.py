my_disk = {}

print(id(my_disk))
print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = 8000


print(my_disk)

# print(my_disk.items())  # выводится специальный объект класса dict_items
# print(type(my_disk.items()))


# print(my_disk.keys())  # выводится специальный объект класса dict_keys
# print(list(my_disk.keys()))  # меняем тип на list (список)

# получаем котеж, метод удалил один элемент, который был удалён
# print(my_disk.popitem())

# print(my_disk.get('type'))  # ответ None, так как такого ключа нет
# print(my_disk['type'])  # KeyError


new_disk = my_disk.copy()
new_disk['tupe'] = 'ssd'

print(new_disk)

print(len(my_disk))
