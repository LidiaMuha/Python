import random


num = int(input("Введите число от 1 до 5: "))
random_num = random.randint(1, 5)

while True:
    num = int(input("Введите число от 1 до 5: "))
    if num != random_num:
        print("Попробуйте снова...")
        continue
    print("Поздравляю!", random_num)
    break
