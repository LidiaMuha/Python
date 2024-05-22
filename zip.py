fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]

fruit_qtys_zip = zip(fruits, quantities)
print(fruit_qtys_zip)

print(type(fruit_qtys_zip))

# fruit_qtys_list = list(fruit_qtys_zip)
# print(fruit_qtys_list)
# [('apple', 100), ('banana', 70), ('lime', 50)]

fruit_qtys_dict = dict(fruit_qtys_zip)
print(fruit_qtys_dict)
# {'apple': 100, 'banana': 70, 'lime': 50}

print('----------------')

product = ['cookies', 'shugar', 'oil', 'water']
price = [80, 30, 150, 15]

product_and_price = zip(product, price)

product_and_price_dict = dict(product_and_price)
print(product_and_price_dict)
