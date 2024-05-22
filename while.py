import random


i = 9

while i < 50:
    print(i)
    i += 10

print('-----')

while True:
    answer = input("Введите да или нет: ")
    if answer == 'нет':
        break

print('-----')


random_num = random.randint(1, 5)

while True:
    num = int(input("Введите число от 1 до 5: "))
    if num != random_num:
        print("Попробуйте снова...")
        continue
    print("Поздравляю!", random_num)
    break
