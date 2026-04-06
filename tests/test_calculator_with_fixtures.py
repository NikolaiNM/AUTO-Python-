# tests/test_calculator.py
import pytest
import sys
import os

# Добавляем путь к src (чтобы работал импорт)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортируем функции из calculator
from src.calculator import add, subtract, multiply, divide, power


class TestAdd:
    """Тесты для сложения"""

    def test_add_positive(self, numbers):
        result = add(numbers["a"], numbers["b"])
        assert result == 15

    def test_add_with_zero(self, numbers, zero):
        result = add(numbers["a"], zero)
        assert result == numbers["a"]

    def test_add_negative(self, numbers, negative):
        result = add(numbers["a"], negative)
        assert result == 7


class TestSubtract:
    """Тесты для вычитания"""

    def test_subtract_positive(self, numbers):
        result = subtract(numbers["a"], numbers["b"])
        assert result == 5

    def test_subtract_negative_result(self, numbers):
        result = subtract(numbers["b"], numbers["a"])
        assert result == -5


class TestMultiply:
    """Тесты для умножения"""

    def test_multiply_positive(self, numbers):
        result = multiply(numbers["a"], numbers["b"])
        assert result == 50

    def test_multiply_by_zero(self, numbers, zero):
        result = multiply(numbers["a"], zero)
        assert result == 0


class TestDivide:
    """Тесты для деления"""

    def test_divide_positive(self, numbers):
        result = divide(numbers["a"], numbers["b"])
        assert result == 2

    def test_divide_by_zero(self, numbers, zero):
        with pytest.raises(ZeroDivisionError):
            divide(numbers["a"], zero)

    def test_divide_returns_float(self, numbers):
        result = divide(7, 2)
        assert result == 3.5
        assert isinstance(result, float)


class TestPower:
    """Тесты для возведения в степень"""

    def test_power_positive(self):
        result = power(2, 3)
        assert result == 8

    def test_power_zero_exponent(self, numbers):
        result = power(numbers["a"], 0)
        assert result == 1