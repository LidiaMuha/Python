import pytest

from calculator.calculator import simple_calculator


# def test_simple_calculator_plus_operation():
#     result = simple_calculator(3, 3, "+")
#     assert result == 6
#
#
# def test_simple_calculator_minus_operation():
#     result = simple_calculator(3, 3, "-")
#     assert result == 0
#
#
# def test_simple_calculator_div_operation():
#     result = simple_calculator(3, 3, "/")
#     assert result == 1
#
#
# def test_simple_calculator_mul_operation():
#     result = simple_calculator(3, 3, "*")
#     assert result == 9


@pytest.mark.parametrize("num_1, num_2, operation, expected_result", [(3, 3, "+", 6),
                                                                      (3, 1, "-", 2),
                                                                      (3, 3, "/", 1),
                                                                      (3, 3, "*", 9)])
def test_simple_calculator(num_1, num_2, operation, expected_result):
    result = simple_calculator(num_1, num_2, operation)
    assert result == expected_result
