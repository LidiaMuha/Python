# Николаю требуется проверить, возможно ли из представленных отрезков условной
# длины сформировать треугольник. Для этого он решил создать класс TriangleChecker,
# принимающий только положительные числа. С помощью метода is_triangle() возвращаются
# следующие значения (в зависимости от ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.

class TriangleChecker:
    # решение задачи по требованию автора

    # def __init__(self, line_1, line_2, line_3):
    #     self.line_1 = line_1
    #     self.line_2 = line_2
    #     self.line_3 = line_3

    # def is_triangle(self):
    #     if (type(self.line_1) is not int) or (type(self.line_2) is not int) or (type(self.line_3) is not int):
    #         return print("Нужно вводить только числа!")
    #     if (self.line_1 < 0) or (self.line_2 < 0) or (self.line_2 < 0):
    #         return print("С отрицательными числами ничего не выйдет!")
    #     if ((self.line_1 + self.line_2) < self.line_3) or ((self.line_1 + self.line_3) < self.line_2) or ((self.line_2 + self.line_3) < self.line_1):
    #         return print("Жаль, но из этого треугольник не сделать")
    #     return print("Ура, можно построить треугольник!")

    # Моё решение задачи: отбирать невалидные данные сразу при инициализации объекта
    def __init__(self, line_1, line_2, line_3):
        self.line_1 = line_1
        self.line_2 = line_2
        self.line_3 = line_3
        if (type(self.line_1) is not int) or (type(self.line_2) is not int) or (type(self.line_3) is not int):
            return print("Нужно вводить только числа!")
        if (self.line_1 < 0) or (self.line_2 < 0) or (self.line_2 < 0):
            return print("С отрицательными числами ничего не выйдет!")
        if ((self.line_1 + self.line_2) < self.line_3) or ((self.line_1 + self.line_3) < self.line_2) or ((self.line_2 + self.line_3) < self.line_1):
            return print("Жаль, но из этого треугольник не сделать")
        return print("Ура, можно построить треугольник!")


triang_two = TriangleChecker(6, 6, 3)
