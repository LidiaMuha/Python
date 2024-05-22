# Задача 1
# Создайте функцию dict_to_list, которая будет конвертировать словарь в список кортежей

# Функция должна принимать словарь, а возвращать список кортежей, в каждом кортеже
# должны быть пары (ket, value) из словаря

# Если значение - целое число, то его нужно умножить на 2 перед добавлением в кортеж

def dict_to_list(my_dict):
    list_for_convertion = []
    for key, value in my_dict.items():
        if type(value) == int:
            value *= 2
        list_for_convertion.append((key, value))
    return list_for_convertion


dict_one = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(dict_to_list(dict_one))

print('-------')


# Задача 2
# Создайте функцию filter_list, которая будет фильтровать список

# У функции должно быть два аргумента - список и тип значения

# Функция должна вернуть новый список, в котором останутся только значения
# того типа, который был передан в вызове функции вторым аргументом

# Функцию можно будет вызвать например так:
# filter_list([35, True, 'abc', 10], int) и получить [35, 10]

def filter_list(my_list, value_type):
    new_list = []
    for el in my_list:
        if type(el) == value_type:
            new_list.append(el)
    return new_list


print(filter_list([35, True, 'abc', 10], int))


print('-------')


# решение задачи 2 через встроенную функцию filter()

def filter_list_two(list_to_filter, value_type_two):
    def check_element_type(elem):
        # return isinstance(elem, value_type_two)
        # или
        return type(elem) is value_type_two
    return filter(check_element_type, list_to_filter)


res = list(filter_list_two([4, True, 6.5, {}], int))
print(res)
# Ответ
# <filter object at 0x102f3e530>
