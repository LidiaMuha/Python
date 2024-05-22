class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


custom_list = ExtendedList([3, 5, 2])

custom_list.print_list_info()
# ЭТО РАСШИРЕНИЕ ФУНКЦИОНАЛА КЛАССА PYTHOM LIST

# видим, что наш список можно дополнять
custom_list.append(7)
custom_list.print_list_info()

# смотрим на собственные атрибуты объекта
print(custom_list.__dict__)
# Ответ: {}
# их нет


# Удостоверимся, что ExtendedList является подклассовм
print(list.__subclasses__())
# Ответ: [<class '_frozen_importlib._List'>, <class '__main__.ExtendedList'>]
