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