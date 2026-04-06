import pytest
import sys
import os

# Добавляем путь к src, чтобы импортировать калькулятор
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import add, subtract, multiply, divide, power


@pytest.mark.smoke
class TestAdd:
    """Тесты функции сложения"""

    def test_add_positiv_numbers(self):
        assert add(10, 3) == 13

    def test_add_negativ_numbers(self):
        assert add(-5, -2) == -7

    def test_add_mixed_numbers(self):
        assert add(7, -3) == 4

    def test_add_double_zeros(self):
        assert add(0, 0) == 0


class TestSubtract:
    """Тесты для функции вычитания"""

    def test_subtract_positive_results(self):
        assert subtract(10, 5) == 5

    def test_subtract_negative_results(self):
        assert subtract(3, 8) == -5

    def test_subtract_zero_results(self):
        assert subtract(5, 5) == 0


class TestMultiply:
    """Тесты для функции умножения"""

    def test_multiply_positive_results(self):
        assert multiply(10, 5) == 50

    def test_multiply_negative_results(self):
        assert multiply(-3, 8) == -24

    def test_multiply_by_zero(self):
        assert multiply(4, 0) == 0


class TestDivide:
    """Тест для функции деления"""

    def test_divide_positive(self):
        assert divide(4, 2) == 2

    def test_divide_float_results(self):
        assert divide (5, 2) == 2.5

    def test_divide_negative_divisible(self):
        assert divide(-6, 3) == -2

    def test_add_debug(self):
        result = add(2, 3)
        print(f"\nResult: {result}")  # \n для переноса строки
        assert result == 5


class TestPower:
    """Тест для функции возведение в степень"""

    def test_pow(self):
        assert power(3, 2) == 9