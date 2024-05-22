# вариант с обычным for in

all_nums = [-3, 1, 0, 10, -20, 5]
absolut_nums = []

for num in all_nums:
    absolut_nums.append(abs(num))

print(absolut_nums)
print(all_nums)

print('------')

# вариант с сокращенным for in

all_nums_2 = [-3, 1, 0, 10, -20, 5]
absolut_nums_2 = [abs(num) for num in all_nums_2]

print(absolut_nums_2)
print(all_nums_2)

print('------')

# формирование нвого списка с фильтрацией

all_nums_3 = [-3, 1, 0, 10, -20, 5]
positiv_nums = [num for num in all_nums_3 if num > 0]

print(positiv_nums)
print(all_nums_3)

print('------')

# создание нового набора, в котром элементы умножены на себя же

my_set = {1, 10, 15}
new_set = set()

for val in my_set:
    new_set.add(val * val)

print(new_set)
print(my_set)

print('------')

# создание нового набора с помощью сокращенного for in

my_set_1 = {1, 10, 15}
# new_set_2 = set((val * val) for val in my_set_1)
new_set_2 = {(val * val) for val in my_set_1}

print(new_set_2)
print(my_set_1)

print('------')

# создание нового словаря

my_scores = {
    'a': 10,
    'b': 7,
    'c': 14
}

scores = {}

for key, value in my_scores.items():  # items возвращает последовательность кортежей и сразу идёт распаковка на пары ключ занчение
    scores[key] = value * 10

print(scores)
print(my_scores)

print('------')

# создание нового словаря for in

my_scores_2 = {
    'a': 10,
    'b': 7,
    'c': 14
}

scores_2 = {key_2: value_2 * 10 for key_2, value_2 in my_scores_2.items()}
print(scores_2)
print(my_scores_2)
