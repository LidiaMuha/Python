class SomeClass():
    def __init__(self, value):
        self._value = value

    def getvalue(self):  # получение значения атрибута
        return self._value

    def setvalue(self, value):  # установка значения атрибута
        self._value = value

    def delvalue(self):  # удаление атрибута
        del self._value

    value = property(getvalue, setvalue, delvalue, "Свойство value")


class Mine(object):

    def __init__(self):
        self._x = None

    x = property()

    @x.getter
    def x(self):
        """Это свойство x."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        self._x = 'No more'


obj = SomeClass(42)
print(obj.value)
obj.value = 43

print(obj.getvalue())

obj.setvalue(0)
print(obj.getvalue())
