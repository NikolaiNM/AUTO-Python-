

def add(a, b):
    """Сложение 2ух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание 2ух чисел"""
    return a - b

def multiply(a, b):
    """Умножение 2ух чисел"""
    return a * b

def divide(a, b):
    """Деление 2ух чисел"""
    if b == 0:
        raise ZeroDivisionError("Divide by zero")
    return a / b

def power(base, exponent):
    """Возведеие в степень"""
    return base ** exponent
