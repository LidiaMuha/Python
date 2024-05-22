my_number = 21.5

if type(my_number) is int:
    print(my_number, "- это целое число")
else:
    print(my_number, "- это нецелое число")


print('-----------')

my_phone = {
    'price': 200,
    'brand': 0
}

if my_phone.get('brand'):
    print("Бренд телефона -", my_phone['brand'])
else:
    print("Бренд телефона не указан")
