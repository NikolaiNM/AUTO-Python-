# tests/conftest.py
import pytest
import sys
import os

# Добавляем путь к src (чтобы работали импорты)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import add, subtract, multiply, divide, power

@pytest.fixture
def numbers():
    """Тестовые данные: пара чисел для операций"""
    return {"a": 10, "b": 5}

@pytest.fixture
def zero():
    """Фикстура для теста с нулём"""
    return 0

@pytest.fixture
def negative():
    """Фикстура для теста с отрицательным числом"""
    return -3


# ===== ФИКСТУРЫ С РЕЗУЛЬТАТАМИ =====

@pytest.fixture
def expected_sum(numbers):
    """Ожидаемый результат сложения"""
    return numbers["a"] + numbers["b"]


@pytest.fixture
def expected_product(numbers):
    """Ожидаемый результат умножения"""
    return numbers["a"] * numbers["b"]