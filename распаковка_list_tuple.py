my_fruits = ['apple', 'banana', 'lime']

my_apple, my_banana, my_lime = my_fruits

print(my_apple, my_banana, my_lime)

my_apple, *new_fruits = my_fruits  # разделение листов
print(my_apple)
print(new_fruits)

print('---------------------------')

my_vegetables = ('cucumber', 'potatoe', 'carrot')

my_cucumber, my_potatoe, my_carrot = my_vegetables

print(my_cucumber, my_potatoe, my_carrot)


# отличие листа от кортежа в том, что в лист можно добалять/удалять новые эелемнты
