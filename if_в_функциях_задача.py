# Создайте функцию route_info, которая будет передавать словарь
# Если в словаре есть ключь distance и его значение - целое число, то верните строку
# "Дистанция равна"
# Иначе, если в словаре есть ключи speed и time, верните строку
# "Дистанция равна"
# Иначе верните строку "Информация невалидна"

def route_info(route_dict):
    if ('distance' in route_dict) and (type(route_dict.get('distance')) is int):
        return f"Дистанция равна {route_dict['distance']}"

    # Ещё вариент
    # if ('distance' in route_dict) and (type(route_dict['distance']) == int):
    #     return f"Дистанция равна {route_dict['distance']}"

    if ('speed' in route_dict) and ('time' in route_dict) and type(route_dict.get('speed')) is int and type(route_dict.get('time')) is int:
        return f"Дистанция равна {route_dict['speed'] * route_dict['time']}"

    return f"Информация невалидна"


my_dict_one = {
    'distance': 5
}

my_dict_two = {
    'speed': 10,
    'time': 5
}

print(route_info(my_dict_one))
print(route_info(my_dict_two))

print('--------')

print(route_info({'distance': 5.5}))
print(route_info({'distance': 55}))
print(route_info({'speed': 10, 'time': 5}))
print(route_info({'speed': 10.3, 'time': 5}))
print(route_info({'time': 5}))
