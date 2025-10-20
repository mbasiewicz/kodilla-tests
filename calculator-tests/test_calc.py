from src.calc import Calculator


# === TESTY ADD ===
def test_add_positive_numbers():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_add_negative_numbers():
    calc = Calculator()
    assert calc.add(-2, -3) == -5


def test_add_negative_and_positive_numbers_result_positive():
    calc = Calculator()
    assert calc.add(-2, 3) == 1


def test_add_negative_and_positive_numbers_result_negative():
    calc = Calculator()
    assert calc.add(-5, 3) == -2


def test_add_with_zero_left():
    calc = Calculator()
    assert calc.add(0, 3) == 3


def test_add_with_zero_right():
    calc = Calculator()
    assert calc.add(5, 0) == 5


def test_add_large_numbers():
    calc = Calculator()
    assert calc.add(9999999999, 1) == 10000000000


# === TESTY SUB ===


def test_sub_positive_numbers():
    calc = Calculator()
    assert calc.sub(4, 3) == 1


def test_sub_negative_numbers():
    calc = Calculator()
    assert calc.sub(-5, -3) == -2


def test_sub_negative_and_positive_numbers_result_positive():
    calc = Calculator()
    assert calc.sub(3, -3) == 6


def test_sub_negative_and_positive_numbers_result_negative():
    calc = Calculator()
    assert calc.sub(-5, 3) == -8


def test_sub_with_zero_left():
    calc = Calculator()
    assert calc.sub(0, 3) == -3


def test_sub_with_zero_right():
    calc = Calculator()
    assert calc.sub(5, 0) == 5


def test_sub_large_numbers():
    calc = Calculator()
    assert calc.sub(9999999999, 1) == 9999999998


# === TESTY MUL ===


def test_mul_positive_numbers():
    calc = Calculator()
    assert calc.mul(3, 4) == 12


def test_mul_negative_numbers():
    calc = Calculator()
    assert calc.mul(-3, -4) == 12


def test_mul_negative_and_positive_numbers():
    calc = Calculator()
    assert calc.mul(3, -3) == -9


def test_mul_with_zero_left():
    calc = Calculator()
    assert calc.mul(0, 3) == 0


def test_mul_with_zero_right():
    calc = Calculator()
    assert calc.mul(5, 0) == 0


def test_mul_large_numbers():
    calc = Calculator()
    assert calc.mul(9999999999, 2) == 19999999998


def test_mul_by_one_left():
    calc = Calculator()
    assert calc.mul(1, 3) == 3


def test_mul_by_one_right():
    calc = Calculator()
    assert calc.mul(4, 1) == 4


# === TESTY DIV ===


def test_div_positive_numbers():
    calc = Calculator()
    assert calc.div(4, 2) == 2


def test_div_negative_numbers():
    calc = Calculator()
    assert calc.div(-9, -3) == 3


def test_div_negative_and_positive_numbers():
    calc = Calculator()
    assert calc.div(9, -3) == -3


def test_div_zero_by_number():
    calc = Calculator()
    assert calc.div(0, 3) == 0


def test_div_by_zero_raises_exception():
    """sprawdzenie czy metoda divide rzuca wyjątek przy dzieleniu przez 0"""
    calc = Calculator()
    import pytest

    with pytest.raises(ZeroDivisionError):
        calc.div(5, 0)


def test_div_number_by_itself():
    calc = Calculator()
    assert calc.div(7, 7) == 1


def test_div_by_one():
    calc = Calculator()
    assert calc.div(7, 1) == 7


def test_div_large_numbers():
    calc = Calculator()
    assert calc.div(10000000000, 2) == 5000000000


def test_div_with_reminder():
    calc = Calculator()
    assert calc.div(7, 2) == 3.5
