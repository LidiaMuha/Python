my_fruits = ('apple', 'banana', 'lime')
other_fruits = ('lime', 'apple', 'banana')

print(my_fruits == other_fruits)  # False
print(id(my_fruits) == id(other_fruits))  # False
# Разные кортежи из-за порядка элементов
print(len(my_fruits))
print(my_fruits[0])
print(my_fruits[-1])  # Получаем последний элемент

# TypeError: 'tuple' object does not support item assignment
# other_fruits[0] = 'lemon'

# TypeError: 'tuple' object doesn't support item deletion
# del my_fruits[0]


users = (
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
)

print(users[1]['user_id'])  # 831

users[1]['user_id'] = 100

print(users[1]['user_id'])


name_1 = 'Lida'
name_2 = 'Danil'
name_3 = 'Julia'

all_names = (name_1, name_2, name_3)
print(all_names)

# Метод для изменения кортежей нет, но есть лазейки
my_tuple = (152, 585, 595)
my_list = list(my_tuple)

my_list.append(6278)
print(my_list)

my_tuple_again = tuple(my_list)
print(my_tuple_again)
