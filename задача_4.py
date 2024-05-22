# Строки в Питоне сравниваются на основании значений символов. Т.е. если
# мы захотим выяснить, что больше: Apple или Яблоко, – то Яблоко окажется
# бОльшим. А все потому, что английская буква A имеет значение 65 (берется
# из таблицы кодировки), а русская буква Я – 1071 (с помощью функции ord()
# это можно выяснить). Такое положение дел не устроило Анну. Она считает,
# что строки нужно сравнивать по количеству входящих в них символов.

# Для этого девушка создала класс RealString и реализовала озвученный
# инструментарий. Сравнивать между собой можно как объекты класса, так и
# обычные строки с экземплярами класса RealString. К слову, Анне понадобилось
# только 3 метода внутри класса (включая __init__()) для воплощения задуманного.

class RealString(str):
    def __init__(self, my_string):
        self.my_string = my_string

    # стравнение объектов
    def my_strings(self, other):
        if (len(self.my_string) > len(other.my_string)):
            return f"Строка '{self.my_string}' больше строки '{other.my_string}'"
        else:
            return f"Строка '{other.my_string}' больше строки '{self.my_string}'"

    # сравнение строк из класса str со строка из класса RealString
    def different_strings(self, other):
        if (len(self.my_string) > len(other)):
            return f"Строка '{self.my_string}' больше строки '{other}'"
        else:
            return f"Строка '{other}' больше строки '{self.my_string}'"


a = RealString('Лидия Павловна')
b = RealString('Мухина')
c = 'Данил Романович'
d = 'Марья Ивановна'

print(type(a.my_string))
print(b.my_string)

print(a.my_strings(b))
print(b.different_strings(c))

print('---------------------')

# --------------------------Решение автора https://smartiqa.ru/python-workbook/class#5


class RealString_two:
    def __init__(self, some_str):
        self.some_str = str(some_str)

    def __eq__(self, other):
        if not isinstance(other, RealString_two):
            other = RealString_two(other)
        return len(self.some_str) == len(other.some_str)

    def __lt__(self, other):
        if not isinstance(other, RealString_two):
            other = RealString_two(other)
        return len(self.some_str) < len(other.some_str)

    def __le__(self, other):
        return self == other or self < other


# Тесты
str1 = RealString_two('Молоко')
str2 = RealString_two('Абрикосы растут')
str3 = 'Золото'
str4 = [1, 2, 3]
print(str1 < str4)
print(str1 >= str2)
print(str1 == str3)

print('---------------------')

# --------------------------Решение автора подправленное


class RealString_three:
    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (str, RealString_three)):
            raise TypeError(
                "Операнд справа должен иметь тип str или RealString_three")
        return other if isinstance(other, str) else other.some_str

    def __init__(self, some_str):
        self.some_str = str(some_str)

    def __eq__(self, other):
        st = self.__verify_data(other)
        return self.some_str == st

    def __lt__(self, other):
        st = self.__verify_data(other)
        return self.some_str < st

    def __le__(self, other):
        st = self.__verify_data(other)
        return self.some_str <= st


# Тесты
str5 = RealString_three('Молоко')
str6 = RealString_three('Абрикосы растут')
str7 = 'Золото'
str8 = [1, 2, 3]
print(str5 < str8)
print(str5 >= str6)
print(str5 == str7)
