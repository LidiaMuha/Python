my_img = ('1920', '1080')

# print(f"{my_img[0]}x{my_img[1]}") if len(
#     my_img) == 2 else print("Некорректный формат изображения")
# или вариант 2 с присваиванием в переменную

info = f"{my_img[0]}x{my_img[1]}" if len(
    my_img) == 2 else "Некорректный формат изображения"

print(info)

print('----------')
# переделать под if else

my_img_two = ('1920', '1080')

if len(my_img_two) == 2:
    print(f"{my_img_two[0]}x{my_img_two[1]}")
else:
    print("Некорректный формат изображения")
