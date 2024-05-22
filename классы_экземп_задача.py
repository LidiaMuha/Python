# Создать класс Image

# У каждого экземпляра класса Image должно быть три атрибута:
# - resolurion
# - title
# - extension

# В классе должен быть метод resize, с помощью котрого можно поменять разрешение изображения.
# Вы должны просто менять значение атрибута resolurion

# Создайте несколько экземпляров класса Image и вызовите метод resize

class Image:

    def __init__(self, resolurion, title, extension):
        self.resolurion = resolurion
        self.title = title
        self.extension = extension

    def resize(self):
        self.resolurion = '1920x1080'

    def retitle(self, default_title='Image'):
        self.title = default_title

    def reextension(self, default_extension='jpg'):
        self.extension = default_extension


my_image = Image('100x100', 'Cat', 'png')
print(my_image.resolurion)
print(my_image.title)
print(my_image.extension)

my_image.resize()

print(my_image.resolurion)

my_image.retitle()

print(my_image.title)

my_image.reextension()

print(my_image.extension)
