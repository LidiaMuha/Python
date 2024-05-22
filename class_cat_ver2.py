from abc import abstractmethod, ABC

# Родительский абстракный класс Животные


class Animal(ABC):
    legs = 4
    eyes = 2
    tail = 1
    size = 'big'
    weight = 10

# Метод издавания звуков

    def call_method(self):
        self.animal_sound = "Дышу и люблю покушать"
        print(self.animal_sound)


# Метод расчёта количества лап в одной семье животного (не реализован)

    @abstractmethod
    def get_count_legs(self):
        pass

# Дочерний класс Кошки


class Cat(Animal):
    __count_cat_childbirth = 0

    # Метод инициализации
    def __init__(self, cat_name):
        self.cat_name = cat_name

# Метод издавания звуков котиков

    def call_method(self):
        self.cat_sound = 'Мяу'
        print(self.cat_sound)


# Метод рождения котят

    def born_cat(self, count_cat):
        if count_cat == 2:
            count_cat += 6
            Cat.__count_cat_childbirth += 1
            return count_cat
        self.count_cat = count_cat
        return self.count_cat

# Кот поел

    def cat_eating(self, weight):
        weight += 0.1
        self.weight = weight
        return self.weight

# Кот умер

    def cat_death(self, count_cat):
        count_cat -= 1
        self.count_cat = count_cat
        return self.count_cat

# Количество лап в семье котика
# не работает, решить позже

    # @property
    # def get_count_legs(self, num, callback_fn):
    #     count_cat = self.callback_fn(num)
    #     count_cat_legs = count_cat * 4
    #     print(count_cat_legs)
    def get_count_legs(self, num):
        self.count_cat = self.born_cat(num)
        self.count_cat_legs = self.count_cat * 4
        print(self.count_cat_legs)

    # Метод для возвращения значения скрытого атрибута
    @staticmethod
    def qty_childbirth():
        return Cat.__count_cat_childbirth

    # Статический метод
    @staticmethod
    def get_cat_name(cat_name):
        return f"Этого котика зовут {cat_name}"


# Создан кот Том
tom = Cat('Том')
# Он мяукает (Класс Cat - полиморф)
tom.call_method()
# У него 2 глаза, 1 хвост, но он маленький
tom.eyes = 2
tom.tail = 1
tom.size = 'small'
# У Тома есть подруга и они родили котят
print(tom.born_cat(2))
# Узнаём сколько раз рождались котята
print(Cat.qty_childbirth())
# Том покушал и стал весить
print(tom.cat_eating(3))
# У Тома и его половинки 6 детей, у каждого по 4 лапы
tom.get_count_legs(2)
# Том умер
print(tom.cat_death(8))
# Том поел
print(tom.cat_eating(5))
# смотрим количество котиков в снмье Тома
print(tom.count_cat)

# Проверка работоспособности ститического метода (нет привязки к объекту)
# print(tom.get_cat_name('Том'))
# print(Cat.get_cat_name('Миша'))


# Проверяем атрибуты экземпляра класса
# print(dir(tom))
