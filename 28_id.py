my_name = 'Lidia'

# Каждый раз новый адрес, тк объект пересоздаётся при каждом запуске кода
print(id(my_name))
print(type(my_name))


long_string = """Очень
длинная
строка"""

print(long_string)
print(len(long_string))  # Длина строки 20
print(long_string[0])
print(long_string[3:7])

print(long_string.replace("длинная", "короткая"))
print(long_string.count('н'))
