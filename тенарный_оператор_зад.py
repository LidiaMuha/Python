# с помощью тернарного оператора проверить длину строки (например, если длина
# строки больше 79 символов, то пишем в терминале, что строка слишком длинная, иначе
# строка короткая)

my_string = "Привет, всем дорогим подписчикам"

print(len(my_string))

print("Строка слишком длинная") if len(my_string) > 79 else print(my_string)
