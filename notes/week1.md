# 📓 Заметки: Неделя 1 — Фундамент: окружение, Git, первые тесты

## 📋 ОГЛАВЛЕНИЕ

- [Python и окружение](#python-и-окружение)
- [Виртуальное окружение (venv)](#виртуальное-окружение-venv)
- [Git — базовые команды](#git--базовые-команды)
- [.gitignore](#gitignore)
- [Структура проекта](#структура-проекта)
- [Первые тесты: калькулятор](#первые-тесты-калькулятор)
- [Запуск тестов с pytest](#запуск-тестов-с-pytest)
- [GitHub: первый пуш](#github-первый-пуш)
- [Для собеседования](#для-собеседования)
- [Вопросы для самопроверки](#вопросы-для-самопроверки)
- [Ссылки](#ссылки)

---

## 🐍 PYTHON И ОКРУЖЕНИЕ

### Установка Python на Windows

1. Скачай с [python.org/downloads](https://www.python.org/downloads/)
2. Запусти установщик
3. ⚠️ **Поставь галочку:** `Add Python to PATH`
4. Нажми `Install Now`

### Проверка установки

```cmd
python --version
# Ожидаемый результат: Python 3.11.x
```

### Установка редактора

**VS Code** (рекомендуется) или **PyCharm Community**.

**Полезные расширения для VS Code:**
- Python (Microsoft)
- Pylance
- GitLens
- pytest

---

## 📦 ВИРТУАЛЬНОЕ ОКРУЖЕНИЕ (VENV)

### Зачем нужно

Изолирует зависимости проекта от системного Python.

### Создание и активация

```cmd
# Перейди в папку проекта
cd Desktop\python-automation-learning

# Создай виртуальное окружение
python -m venv venv

# Активируй (Windows)
venv\Scripts\activate

# Проверка: должен появиться префикс (venv)
(venv) C:\...\python-automation-learning>
```

### Работа с пакетами

```cmd
# Установка pytest
pip install pytest pytest-html

# Просмотр установленных пакетов
pip list

# Сохранение зависимостей
pip freeze > requirements.txt

# Установка из файла
pip install -r requirements.txt

# Деактивация окружения
deactivate
```

### Частые команды

| Команда | Что делает |
|---------|-----------|
| `python -m venv venv` | Создаёт окружение в папке venv/ |
| `venv\Scripts\activate` | Активирует окружение |
| `deactivate` | Выход из окружения |
| `pip install <package>` | Устанавливает пакет |
| `pip freeze > requirements.txt` | Сохраняет список пакетов |
| `where python` | Показывает путь к активному Python |

---

## 📦 GIT — БАЗОВЫЕ КОМАНДЫ

### Первоначальная настройка

```cmd
git config --global user.name "Твоё Имя"
git config --global user.email "твоя@почта.com"
```

### Основные команды

```cmd
# Инициализация репозитория
git init

# Проверка статуса
git status

# Добавление файлов
git add .                    # все файлы
git add <файл>              # конкретный файл

# Коммит
git commit -m "feat: сообщение"

# Просмотр истории
git log
git log --oneline           # кратко

# Отправка на GitHub
git push -u origin main
```

### Префиксы коммитов

| Префикс | Когда использовать |
|---------|-------------------|
| `feat:` | Новая функция |
| `fix:` | Исправление бага |
| `docs:` | Изменения в документации |
| `refactor:` | Рефакторинг кода |
| `test:` | Добавление тестов |
| `chore:` | Настройка, конфиги |

**Пример:**

```cmd
git commit -m "feat: add calculator functions"
git commit -m "fix: handle division by zero"
```

---

## 📄 .GITIGNORE

### Зачем нужен

Чтобы не коммитить мусор: временные файлы, окружение, секреты.

### Что добавить для Python-проекта

```
# Виртуальное окружение
venv/
env/
.venv/

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# Тесты и отчёты
.pytest_cache/
.coverage
htmlcov/
*.cover
report.html

# Логи и временные файлы
*.log
logs/
tmp/
temp/

# Секреты
.env
.env.local
*.key
*.pem

# IDE
.idea/
.vscode/
*.swp
*.swo

# ОС
.DS_Store
Thumbs.db
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
│   ├── conftest.py         # Фикстуры (позже)
│   └── test_calculator.py  # Тесты
├── .gitignore
├── requirements.txt
├── README.md
└── notes/
    └── week1.md
```

### Почему так

- `src/` — исходный код, отдельно от тестов
- `tests/` — тесты, легко находить
- `conftest.py` — общие фикстуры для pytest
- `.gitignore` — не коммитим мусор

---

## 🧪 ПЕРВЫЕ ТЕСТЫ: КАЛЬКУЛЯТОР

### `src/calculator.py`

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

### `tests/test_calculator.py`

```python
import pytest
import sys
import os

# Путь к src (чтобы работал импорт)
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

### Почему `sys.path.insert`

- Тесты лежат в `tests/`, код в `src/`
- Python не видит `src/` по умолчанию
- Эта строка добавляет корень проекта в путь поиска модулей

---

## 🧪 ЗАПУСК ТЕСТОВ С PYTEST

### Базовые команды

```cmd
pytest                    # все тесты
pytest -v                 # подробно (имена тестов)
pytest -s                 # показать print() в тестах
pytest -x                 # стоп на первой ошибке
pytest -k "add"           # фильтр по имени теста
pytest --html=report.html # HTML-отчёт
```

### Установка плагинов

```cmd
# HTML-отчёты
pip install pytest-html

# Allure (продвинутые отчёты)
pip install allure-pytest
```

### Символы в отчёте

| Символ | Значение |
|--------|----------|
| `.` | ✅ passed |
| `F` | ❌ failed |
| `E` | 💥 error |
| `s` | ⏭ skipped |
| `x` | 🟣 xfail |

---

## 🐙 GITHUB: ПЕРВЫЙ ПУШ

### Создание репозитория

1. Зайди на [github.com](https://github.com)
2. Нажми `+` → `New repository`
3. Имя: `python-automation-learning`
4. ✅ Public
5. ✅ Add README
6. ✅ Add .gitignore → Python
7. Нажми `Create repository`

### Отправка кода

```cmd
# Инициализация (если ещё не сделал)
git init

# Добавление файлов
git add .

# Первый коммит
git commit -m "feat: initial commit with calculator and tests"

# Связь с GitHub (замени YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/python-automation-learning.git

# Переименование ветки
git branch -M main

# Отправка
git push -u origin main
```

### Проверка

- Открой репозиторий на GitHub
- Убедись, что файлы появились
- Проверь, что `venv/` и `__pycache__/` не закоммичены

---

## 🗣️ ДЛЯ СОБЕСА

**Зачем нужно виртуальное окружение?**

> Чтобы изолировать зависимости проекта от системного Python. Каждый проект имеет свои пакеты в своей папке venv/, что предотвращает конфликты версий.

**Чем `pip install` отличается от `pip freeze`?**

> `install` — устанавливает пакеты, `freeze` — показывает установленные пакеты с версиями (используется для requirements.txt).

**Зачем нужен `.gitignore`?**

> Чтобы не коммитить файлы, которые генерируются автоматически или содержат секреты: venv/, __pycache__/, .idea/, *.log, .env.

**Что такое pytest?**

> Фреймворк для тестирования на Python. Проще unittest: использует обычный `assert` вместо `self.assertEqual()`, имеет фикстуры, параметризацию и богатую экосистему плагинов.

**Как работает `sys.path.insert` для импортов?**

> Добавляет указанную папку в начало списка путей поиска модулей Python. Нужно, когда тесты и исходный код лежат в разных папках.

**Что означает префикс `feat:` в коммите?**

> Это конвенция коммитов: `feat:` = новая функция, `fix:` = исправление бага, `docs:` = документация. Помогает читать историю изменений.

---

## ❓ ВОПРОСЫ ДЛЯ САМОПРОВЕРКИ

1. Как создать виртуальное окружение на Windows?
2. Как активировать venv в командной строке?
3. Что делает `pip freeze > requirements.txt`?
4. Какие файлы обязательно игнорировать в `.gitignore` для Python?
5. Как запустить тесты с подробным выводом?
6. Как проверить, какой Python сейчас активен?
7. Что означает флаг `pytest -x`?
8. Как добавить все изменённые файлы в Git одной командой?
9. Что такое `conftest.py` и зачем он нужен?
10. Как проверить, что файл попал в `.gitignore`?

---

## 🔗 ССЫЛКИ

- [Python downloads](https://www.python.org/downloads/)
- [pytest документация](https://docs.pytest.org)
- [Git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [GitHub Guides](https://guides.github.com/)
- [VS Code Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [PyCharm Community](https://www.jetbrains.com/pycharm/download/)

---

## 📝 ЛИЧНЫЕ ЗАМЕТКИ

### Инсайты



### Ошибки и решения



### Вопросы для ментора



### Время затрачено

- Всего: __ часов

---

## ✅ ЧЕК-ЛИСТ НЕДЕЛИ 1

- [ ] Python 3.11+ установлен и работает (`python --version`)
- [ ] VS Code / PyCharm настроен с расширениями
- [ ] Виртуальное окружение создаётся и активируется
- [ ] pytest установлен, тесты запускаются (`pytest -v`)
- [ ] `requirements.txt` создан и актуален
- [ ] Git установлен, имя и почта настроены
- [ ] `.gitignore` создан и работает
- [ ] Проект имеет правильную структуру (src/, tests/)
- [ ] Написан калькулятор с 5 функциями
- [ ] Написаны тесты для всех функций
- [ ] Код загружен на GitHub
- [ ] README.md написан
- [ ] Понимаю, зачем нужен `sys.path.insert`