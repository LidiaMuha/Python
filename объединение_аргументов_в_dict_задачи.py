# Перепишите вызов функции merge_list_to_dict из предыдущей задачи так,
# чтоб в нём использовались аргументы с ключевыми словами

def merge_list_to_dict(list_one, list_two):
    c = dict(zip(list_one, list_two))
    return c


res = merge_list_to_dict(
    list_two=[1, 2, 3], list_one=['cucumber', 'tomato', 'potatoe'])

print(res)

# Добавить ещё один вызов функции, в котором будет один
# позиционный аргумент, а второй - аргумент с ключевым словом

res_2 = merge_list_to_dict(
    ['cucumber', 'tomato', 'potatoe'], list_two=[1, 2, 3])
print(res_2)
# НО в ином порядке, когда сначаоа именованный потом позиционный, код не отработает

print('-------------------')


def update_car_info(**car):
    print(car)
    info = {
        f"This car {car['brand']} "
        f"and it has price {car['price']}$"
    }
    car['is_available'] = True
    return info, car


car_1 = update_car_info(brand='BMW', price=1000)
print(car_1)
