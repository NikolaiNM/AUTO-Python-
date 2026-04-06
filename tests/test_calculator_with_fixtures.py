# tests/test_calculator.py
import pytest
import sys
import os

# Путь к src
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
))

from src.calculator import add, subtract, multiply, divide, power


# ====== ADD ======
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (1, 2, 3),
    (7, 0, 7),
    (0, 8, 8),
    (0, 0, 0),
    (-5,-10, -15),
    (5, -5, 0),
    (6, -9, -3),
    (-9, 3, -6),
    (10, -7, 3)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# ===== SUBTRACT =====
@pytest.mark.parametrize("a,b,expected", [
    (10, 5, 5),
    (5, 10, -5),
    (0, 0, 0),
    (-5, -5, 0),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


# ===== MULTIPLY =====
@pytest.mark.parametrize("a,b,expected", [
    (3, 4, 12),
    (5, 0, 0),
    (-2, 5, -10),
    (-2, -3, 6),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


# ===== DIVIDE (успешные случаи) =====
@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (9, 3, 3),
    (7, 2, 3.5),
    (0, 5, 0),
    (-10, 2, -5),
])
def test_divide_success(a, b, expected):
    assert divide(a, b) == expected

# ====== DIVIDE (ошибки) ======
@pytest.mark.parametrize("a, b", [
    (10, 0),
    (5, 0),
    (0, 0),
    (-7, 0)
])
def test_devide_by_zero(a, b):
    with pytest.raises(ZeroDivisionError):
        divide(a, b)

# ===== POWER =====
@pytest.mark.parametrize("base,exp,expected", [
    (2, 3, 8),
    (5, 0, 1),
    (2, -1, 0.5),
    (10, 2, 100),
])
def test_power(base, exp, expected):
    assert power(base, exp) == expected