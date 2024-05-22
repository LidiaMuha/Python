posts_ids = [151, 245, 762, 167]
print(posts_ids[0])  # 151
print(posts_ids[1])  # 245
print(posts_ids[-1])  # 167

# Удвление элемента из списка (функция)
del posts_ids[1]
print(posts_ids)

# Список со словарём с последующим выводом имени пользователя по индексу
users = [
    {
        'user_id': 100,
        'user_name': 'Alice'
    },
    {
        'user_id': 101,
        'user_name': 'Tom'
    }
]

print(len(users))
print(users[0]['user_name'])


happy_num = []
happy_num.append(1)
happy_num.append(2)
happy_num.append(3)
happy_num.append(4)
print(happy_num)
print(len(happy_num))

del happy_num[0]
print(happy_num)


# Удаление элемента из списка (метод класса)
happy_num.pop(1)


removes_elements = [happy_num.pop(0)]
print(removes_elements)

# Сортировка элементов
object_ids = [489, 948, 392, 5950, 39]
object_ids.sort()  # Сортировка по возрастанию
print(object_ids)
object_ids.sort(reverse=True)
print(object_ids)


greeting = "Hello from Python"
greeting_list = list(greeting)
print(greeting_list)


# Конвертация словаря в лист. Значения ключей утеряны
my_dict = {'a': 1, 'b': 2}
my_list = list(my_dict)
print(my_list)


ratings = [2.5, 5.7, 8.11, 0.4]
first_two_retings = ratings[:2]
print(first_two_retings)
