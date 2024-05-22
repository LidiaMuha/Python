my_motorbike = {
    'brand': 'Ducati',
    'price_info': {
        'price': 25000,
        'is_avaliable': True
    },
    'engine_vol': 1.2
}

print(my_motorbike['price_info']['price'])

other_motorbike = {
    'engine_vol': 1.2,
    'price': 25000,
    'brand': 'Ducati',
}

print(my_motorbike == other_motorbike)
print(id(my_motorbike) == id(other_motorbike))

print(my_motorbike['price_info'])

my_motorbike['price_info']['price'] = 20000
print(my_motorbike['price_info'])

my_motorbike['is_new'] = 8545789

print(my_motorbike)

del my_motorbike['is_new']

print(my_motorbike)

key_name = 'brand'
my_motorbike[key_name] = 'BMW'

print(my_motorbike, "\n", key_name)


print(len(other_motorbike))

del other_motorbike['engine_vol']
print(len(other_motorbike))


# Поиск ключа в словаре
print(my_motorbike.get('price'))
# None
