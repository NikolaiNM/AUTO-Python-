# 📓 Заметки: Неделя 1 — Настройка окружения

## 📋 ОГЛАВЛЕНИЕ

- [Окружение (Windows)](#-окружение-windows)
- [Git — базовые команды](#-git--базовые-команды)
- [Структура проекта](#-структура-проекта)
- [Первые тесты](#-первые-тесты)
- [Вопросы для самопроверки](#-вопросы-для-самопроверки)

---

## ⚙️ ОКРУЖЕНИЕ (Windows)

### Виртуальное окружение

```cmd
# Создание
python -m venv venv

# Активация
venv\Scripts\activate

# Деактивация
deactivate
```

### Пакеты

```cmd
# Установка pytest
pip install pytest pytest-html

# Сохранение зависимостей
pip freeze > requirements.txt

# Установка из файла
pip install -r requirements.txt
```

### Проверка

```cmd
python --version
pytest --version
where python
```

---

## 📦 GIT — БАЗОВЫЕ КОМАНДЫ

### Инициализация

```cmd
git init
git add .
git commit -m "feat: сообщение"
git push
```

### Настройка

```cmd
git config --global user.name "Имя"
git config --global user.email "email"
```

### Проверка

```cmd
git status
git log --oneline
```

### .gitignore — что игнорировать

```
venv/
__pycache__/
*.pyc
.pytest_cache/
.coverage
htmlcov/
*.log
.env
.idea/
.vscode/
```

### Если файл уже в Git

```cmd
# Удалить из отслеживания, но оставить на диске
git rm -r --cached __pycache__/
git commit -m "chore: remove __pycache__ from tracking"
```

---

## 📁 СТРУКТУРА ПРОЕКТА

```
python-automation-learning/
├── src/
│   └── calculator.py       # Функции калькулятора
├── tests/
│   ├── conftest.py         # Фикстуры
│   └── test_calculator.py  # Тесты
├── .gitignore
├── requirements.txt
├── README.md
└── notes/
    └── week1.md
```

---

## 🧪 ПЕРВЫЕ ТЕСТЫ

### calculator.py

```python
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
    """Возведение в степень"""
    return base ** exponent
```

### test_calculator.py

```python
import pytest
import sys
import os

# Путь к src
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
))

from src.calculator import add, subtract, multiply, divide, power


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_power():
    assert power(2, 3) == 8
```

### Запуск тестов

```cmd
pytest                    # все тесты
pytest -v                 # подробно
pytest --html=report.html # HTML-отчёт
```

---

## 🗣️ ДЛЯ СОБЕСА

**Зачем нужно виртуальное окружение?**
> Чтобы изолировать зависимости проекта от системного Python. Каждый проект имеет свои пакеты в своей папке venv/.

**Чем pip install отличается от pip freeze?**
> `install` — устанавливает пакеты, `freeze` — показывает установленные (для requirements.txt).

**Зачем нужен .gitignore?**
> Чтобы не коммитить мусор: venv/, __pycache__/, .idea/, *.log, секреты.

**Что такое pytest?**
> Фреймворк для тестирования на Python. Проще unittest: использует assert вместо self.assertEqual(), имеет фикстуры и плагины.

---

## ❓ ВОПРОСЫ ДЛЯ САМОПРОВЕРКИ

1. Как создать виртуальное окружение?
2. Как активировать venv на Windows?
3. Что делает `pip freeze > requirements.txt`?
4. Какие файлы обязательно игнорировать в .gitignore?
5. Как запустить тесты с подробным выводом?
6. Как проверить, что файл попал в .gitignore?
7. Что означает префикс `feat:` в коммите?

---

## 🔗 ССЫЛКИ

- [pytest документация](https://docs.pytest.org)
- [Git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Python docs](https://docs.python.org/3/)
- [GitHub docs](https://docs.github.com/)

---

## 📝 ЛИЧНЫЕ ЗАМЕТКИ

### Инсайты



### Ошибки и решения



### Вопросы для ментора



### Время затрачено

- Всего: __ часов

---

## ✅ ЧЕК-ЛИСТ НЕДЕЛИ 1

- [ ] Python 3.11+ установлен
- [ ] Виртуальное окружение создаётся и активируется
- [ ] pytest установлен, тесты запускаются
- [ ] Git настроен (имя, почта)
- [ ] .gitignore создан и работает
- [ ] Проект загружен на GitHub
- [ ] README.md написан
- [ ] Первые тесты написаны и проходят

---
