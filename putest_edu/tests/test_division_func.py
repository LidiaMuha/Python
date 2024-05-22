from putest_edu.utils import division
import pytest


# спец дикоратор, которму мы передаём строку с переменными, которые мы будем использовать
# мы хотим праметризовать наш тест
# внутри произойдёт рапаковка кортежа (a, b, expected_result = (10, 2, 5))
@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result
# assert проверяет является ли результат выражения значением true


@pytest.mark.parametrize("expected_exception, arg_one, arg_two", [(ZeroDivisionError, 10, 0), (TypeError, 5, "2")])
# тест на проверку ошибок
def test_division_with_error(expected_exception, arg_one, arg_two):
    with pytest.raises(expected_exception):  # указываем исключение
        division(arg_one, arg_two)
