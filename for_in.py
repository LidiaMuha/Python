my_list = [True, 10, 'abc', {}]

for elem in my_list:
    print(elem)

# Ответ
# True
# 10
# abc
# {}

print('--------')

my_tuple = ('1920x1080', True, 27)

for elem in my_tuple:
    print(elem)
# Ответ
# 1920x1080
# True
# 27

print('--------')

my_set = {1435, 4317, 2761, 5721}

for id in my_set:
    print(id)
# Ответ
# 5721
# 1435
# 2761
# 4317

print('--------')

for num in range(5):
    print(num)
# Ответ
# 0
# 1
# 2
# 3
# 4

print('--------')

for odd_num in range(3, 10, 2):
    print(odd_num)
# Ответ
# 3
# 5
# 7
# 9

print('--------')

my_dict = {
    'x': 10,
    'y': True,
    'z': 'abc'
}

# for key in my_dict:
#     print(key, ':', my_dict[key])

# Ответ
# x : 10
# y : True
# z : abc

# item - это кортеж (каждый кортеж - это пара ключ-значение),
# метод items() возвращает кортеж типа dict_items
for item in my_dict.items():
    print(item)
    key, value = item  # распаковка кортежа
    print(key, value)

# Ответ
# x 10
# y True
# z abc


# или вариант 2, где распаковка идёт сразу после for

for key, value in my_dict.items():
    print(key, value)
