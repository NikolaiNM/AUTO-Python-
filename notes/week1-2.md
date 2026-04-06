# 📓 Заметки: Недели 1-2 — Основы и pytest

## 📋 ОГЛАВЛЕНИЕ
1. Окружение (Windows)
2. Git — базовые команды
3. Структура проекта
4. pytest — база
5. Фикстуры
6. Встроенные фикстуры
7. Для собеседования
8. Вопросы для самопроверки
9. Ссылки

---

## ⚙️ ОКРУЖЕНИЕ (Windows)

# Виртуальное окружение
python -m venv venv
venv\Scripts\activate
deactivate

# Пакеты
pip install pytest pytest-html
pip freeze > requirements.txt
pip install -r requirements.txt

# Проверка
python --version
pytest --version
where python

---

## 📦 GIT — БАЗОВЫЕ КОМАНДЫ

# Инициализация
git init
git add .
git commit -m "feat: сообщение"
git push

# Настройка
git config --global user.name "Имя"
git config --global user.email "email"

# Проверка
git status
git log --oneline

# .gitignore — что игнорировать:
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

---

## 📁 СТРУКТУРА ПРОЕКТА

python-automation-learning/
├── src/calculator.py       # Функции: add, subtract, multiply, divide, power
├── tests/
│   ├── conftest.py         # Фикстуры (доступны без импорта)
│   └── test_calculator.py  # Тесты
├── .gitignore
├── requirements.txt
├── README.md
└── notes/week1-2.md

---

## 🧪 PYTEST — БАЗА

# Конвенции именования:
- Файлы: test_*.py или *_test.py
- Функции: def test_*():
- Классы: class Test* (без __init__)

# Запуск тестов:
pytest                    # все тесты
pytest -v                 # подробно
pytest -s                 # показать print()
pytest -x                 # стоп на первой ошибке
pytest -k "add"           # фильтр по имени
pytest --maxfail=3        # стоп после 3 ошибок
pytest --tb=short         # краткий стектрейс
pytest --html=report.html # HTML-отчёт

# Символы в отчёте:
. = passed ✅
F = failed ❌
E = error 💥
s = skipped ⏭
x = xfail 🟣

# Assert vs unittest:
# ✅ pytest — просто
assert add(2, 3) == 5

# ❌ unittest — многословно
self.assertEqual(add(2, 3), 5)

---

## 🎁 ФИКСТУРЫ

# Синтаксис:
import pytest

@pytest.fixture
def my_fixture():
    setup()
    yield value      # тест получает это
    teardown()       # выполнится всегда

# Scope (область видимости):
- function (default) — перед каждым тестом
- class — один раз на класс
- module — один раз на файл
- session — один раз на весь прогон

# conftest.py:
- Фикстуры доступны во всех тестах БЕЗ импорта
- Лежит в tests/ или подпапках
- НЕ делится импортами, только фикстурами!
- sys.path.insert не нужен, если нет импортов

# Когда использовать ✅:
- Дорогостоящая настройка (БД, браузер, API)
- Одинаковые сложные данные в 10+ тестах
- Автоматическая очистка ресурсов
- Моки и заглушки

# Когда НЕ использовать ❌:
- Простые данные (числа, строки) — пиши явно в тесте
- Когда фикстура скрывает смысл теста
- Когда тест становится менее читаемым

# Пример ХОРОШО:
def test_add_two_positive_numbers():
    """10 + 5 = 15"""
    result = add(10, 5)
    assert result == 15

# Пример ПЛОХО:
def test_add(self, numbers):
    result = add(numbers["a"], numbers["b"])
    assert result == 15  # ??? Какие числа?

---

## 🛠 ВСТРОЕННЫЕ ФИКСТУРЫ

- tmp_path — Временная папка (авто-очистка)
- tmp_path_factory — Фабрика временных папок (session)
- capfd — Перехват print()
- caplog — Перехват логов
- monkeypatch — Мокирование ENV

---

## 🗣️ ДЛЯ СОБЕСА

**Что такое фикстуры?**
Функции для подготовки окружения тестов. Позволяют вынести setup/teardown в одно место, переиспользовать код и гарантировать очистку даже при падении теста.

**Что такое conftest.py?**
Специальный файл, где объявленные фикстуры автоматически доступны во всех тестах без импорта.

**Какие scope у фикстур?**
function (каждый тест), class (на класс), module (на файл), session (на весь прогон).

**Почему pytest лучше unittest?**
Меньше бойлерплейта, умные сообщения об ошибках, фикстуры вместо setUp/tearDown, богатая экосистема плагинов.

**Встроенные фикстуры?**
tmp_path (временная папка), capfd (перехват print), caplog (логи), monkeypatch (моки ENV).

---

## ❓ ВОПРОСЫ ДЛЯ САМОПРОВЕРКИ

1. Чем pip install отличается от pip freeze?
2. Зачем нужен yield в фикстуре?
3. Почему тесты лучше писать с явными данными?
4. Как запустить только тесты с "add" в имени?
5. Что выполнится после yield, если тест упал?
6. Зачем нужен .gitignore?
7. Как называется файл с фикстурами, доступными везде?

---

## 🔗 ССЫЛКИ

- pytest официальная документация: https://docs.pytest.org
- Fixtures guide: https://docs.pytest.org/en/stable/explanation/fixtures.html
- Parametrize docs: https://docs.pytest.org/en/stable/how-to/parametrize.html
- Git cheat sheet: https://education.github.com/git-cheat-sheet-education.pdf
- Python docs: https://docs.python.org/3/

---

## 📝 ЛИЧНЫЕ ЗАМЕТКИ

### Инсайты


### Ошибки и решения


### Вопросы для ментора


### Время затрачено
- Неделя 1: __ часов
- Неделя 2: __ часов

---

## ✅ ЧЕК-ЛИСТ

- [ ] Python 3.11+ установлен
- [ ] Виртуальное окружение работает
- [ ] pytest установлен, тесты запускаются
- [ ] Git настроен, код на GitHub
- [ ] .gitignore создан
- [ ] Понимаю конвенции pytest
- [ ] Понимаю фикстуры и когда использовать
- [ ] Создал conftest.py
- [ ] Тесты читаются как документация