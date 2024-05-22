# Создайте функцию image_info с одним параметров типа dict

# Функция ожидает словарь, в котором должно быть как минимум два ключа:
# image_id и image_title

# Функция должна возвращать строку такого вида
# "Image 'my cat' has id 5136"

# Если хотя бы одного ключа из этих ключей в словаре нет, функция
# должна генерировать ошибку TypeError

def image_info(**my_dict):
    print(my_dict)
    if 'image_title' not in my_dict or 'image_id' not in my_dict:
        raise TypeError("В словаре не переданы обязательные ключи")
    return f"Image '{my_dict['image_title']}' has id {my_dict['image_id']}"


try:
    print(image_info(image_title='my cat', image_id=5136))
except TypeError as a:
    print(a)
else:
    print("Код выполнен без ошибок")
