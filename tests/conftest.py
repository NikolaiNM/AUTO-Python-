import pytest


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

@pytest.fixture
def calc():
    return Calculator()

# tests/test_calculator.py
@pytest.mark.parametrize("a,b,expected", [
    (10, 5, 15),
    (0, 0, 0),
    (-5, 5, 0),
])
def test_add_with_fixture(a, b, expected, calc):
    """calc — фикстура из conftest.py"""
    result = calc.add(a, b)
    assert result == expected