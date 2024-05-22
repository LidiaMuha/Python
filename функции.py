def my_fn(a, b):
    a = a + 1
    c = a + b
    return c


res = my_fn(10, 3)
print(res)

print('------------------------------------')
# ------------------------------------


def increase_person_age(person):
    person_copy = person.copy()  # копируем объект
    person_copy['age'] += 1  # копию изменяем
    return person_copy  # копию возвращаем


person_one = {
    'name': 'Lidia',
    'age': 25
}

# копию кладём в переменную
new_version_peson = increase_person_age(person_one)
print(person_one['age'])  # оригинальный объект
print(new_version_peson['age'])  # копия объекта
