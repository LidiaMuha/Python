# Создайте функцию merge_list_to_dict
def merge_list_to_dict(a, b):
    c = dict(zip(a, b))
    return c

# У функции должно быть два аргумента
# Функция должна объединять два списка, используя встроенную функцию zip
# Конвертируйте объект zip в словарь верните из функции
# Выведите результат функции в терминал


list_one = ['cucumber', 'tomato', 'potatoe']
list_two = [1, 2, 3]

res = merge_list_to_dict(list_one, list_two)
print(res)


res_two = merge_list_to_dict(['v'], [{}, True, 100])
print(res_two)  # {'v': {}}


# res_three = merge_list_to_dict([{}, True, 100], ['v'])
# print(res_three)  # TypeError: unhashable type: 'dict'

res_four = merge_list_to_dict([56, True, 100], ['v'])
print(res_four)  # {56: 'v'}
