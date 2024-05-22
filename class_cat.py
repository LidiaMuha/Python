from abc import abstractmethod, ABC

# Родительский абстракный класс Животные


class Animal(ABC):
    legs = 4
    eyes = 2
    tail = 1
    size = 'big'
    weight = 10

# Метод издавания звуков

    def call_animal_method(self):
        print("Дышу и люблю покушать")


# Метод расчёта количества лап в одной семье животного (не реализован)

    @abstractmethod
    def get_count_legs(self):
        pass

# Дочерний класс Кошки


class Cat(Animal):
    count_cat = 1

    def __init__(self, cat_name):
        self.cat_name = cat_name

# Метод издавания звуков котиков

    def call_cat_method(self):
        print('Мяу')


# Метод рождения котят

    def born_cat(self, count_cat):
        self.count_cat = count_cat
        if count_cat >= 2:
            count_cat += 6
            return count_cat

# Кот поел

    def cat_eating(self, weight):
        self.weight = weight
        weight += 0.1
        return weight

# Кот умер

    def cat_death(self, count_cat):
        self.count_cat = count_cat
        count_cat -= 1
        return count_cat

# Количество лап в семье котика
# не работает, решить позже

    # @property
    # def get_count_legs(self, num, callback_fn):
    #     count_cat = self.callback_fn(num)
    #     count_cat_legs = count_cat * 4
    #     print(count_cat_legs)
    def get_count_legs(self, num):
        count_cat = self.born_cat(num)
        count_cat_legs = count_cat * 4
        print(count_cat_legs)


# Создан кот Том
tom = Cat('Том')
# Он мяукает
tom.call_cat_method()
# Но и является животным
tom.call_animal_method()
# У него 2 глаза, 1 хвост, но он маленький
tom.eyes = 2
tom.tail = 1
tom.size = 'small'
# У Тома есть подруга и они родили котят
print(tom.born_cat(2))
# Том покушал и стал весить
print(tom.cat_eating(3))
# У Тома и его половинки 6 детей, у каждого по 4 лапы
# tom.get_count_legs(2, born_cat)
tom.get_count_legs(2)
# tom.get_count_legs(8, born_cat)
# Том умер
print(tom.cat_death(8))
# Том поел
print(tom.cat_eating(5))
