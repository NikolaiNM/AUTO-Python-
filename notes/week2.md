# 📓 Заметки: Неделя 2 — pytest основы

## 📋 ОГЛАВЛЕНИЕ

- [unittest и pytest — что это](#unittest-и-pytest--что-это)
- [Сравнение unittest vs pytest](#сравнение-unittest-vs-pytest)
- [pytest — база](#pytest--база)
- [Фикстуры](#фикстуры)
- [Параметризация](#параметризация)
- [conftest.py](#conftestpy)
- [Маркеры и селективный запуск](#маркеры-и-селективный-запуск)
- [Для собеседования](#для-собеседования)
- [Вопросы для самопроверки](#вопросы-для-самопроверки)
- [Ссылки](#ссылки)

---

## 📦 UNITTEST И PYTEST — ЧТО ЭТО

### 🔹 unittest

Встроенный фреймворк Python для тестирования. Идёт "из коробки".

**Особенности:**
- Не требует установки
- Построен на классах (`unittest.TestCase`)
- Использует `self.assertEqual()`, `self.assertTrue()`
- Имеет `setUp()` / `tearDown()`

**Пример:**

```python
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)
    
    def setUp(self):
        self.value = 10
```

---

### 🔹 pytest

Сторонний фреймворк — индустриальный стандарт.

**Особенности:**
- Требует установки: `pip install pytest`
- Простой `assert` вместо `self.assertEqual()`
- Фикстуры (`@pytest.fixture`) вместо `setUp/tearDown`
- Параметризация, маркеры, 1000+ плагинов
- Умные сообщения об ошибках

**Пример:**

```python
import pytest

def test_add():
    assert 2 + 2 == 4

@pytest.fixture
def value():
    return 10
```

---

### 🧭 Когда что использовать

| Ситуация | Выбор | Почему |
|----------|-------|--------|
| Новый проект | pytest | Современный, проще поддерживать |
| Legacy-код | unittest | Уже написан |
| Собеседование | Знать оба | Спросят различия |
| Обучение | unittest → pytest | Покажет эволюцию |

---

## 📊 СРАВНЕНИЕ UNITTEST vs PYTEST

| Критерий | unittest | pytest |
|----------|----------|--------|
| Синтаксис | Многословный, ООП | Простой, функциональный |
| Assert | `self.assertEqual()` | `assert` |
| Setup/Teardown | `setUp()`, `tearDown()` | Фикстуры с `yield` |
| Параметризация | `subTest()` (неудобно) | `@pytest.mark.parametrize` |
| Плагины | Ограниченные | 1000+ |
| Отчёты об ошибках | Базовые | Детальные с сравнением |
| Запуск | `python -m unittest` | `pytest` |
| Совместимость | — | Запускает unittest тесты |

---

### Сообщения об ошибках

**unittest:**

```
AssertionError: 5 != 6
```

**pytest:**

```
E       assert 5 == 6
E        +  where 5 = add(2, 3)
E         - 6
E         + 5
```

---

## 🧪 PYTEST — БАЗА

### Конвенции именования

- Файлы: `test_*.py` или `*_test.py`
- Функции: `def test_*():`
- Классы: `class Test*` (без `__init__`)

### Запуск тестов

```cmd
pytest                    # все тесты
pytest -v                 # подробно
pytest -s                 # показать print()
pytest -x                 # стоп на первой ошибке
pytest -k "add"           # фильтр по имени
pytest --maxfail=3        # стоп после 3 ошибок
pytest --tb=short         # краткий стектрейс
pytest --html=report.html # HTML-отчёт
```

### Символы в отчёте

- `.` = passed ✅
- `F` = failed ❌
- `E` = error 💥
- `s` = skipped ⏭
- `x` = xfail 🟣

---

## 🎁 ФИКСТУРЫ

### Синтаксис

```python
import pytest

@pytest.fixture
def my_fixture():
    setup()
    yield value      # тест получает это
    teardown()       # выполнится всегда
```

### Scope (область видимости)

| Scope | Когда создаётся | Пример |
|-------|----------------|--------|
| `function` (default) | Перед каждым тестом | Тестовые данные |
| `class` | Один раз на класс | Тесты одного класса |
| `module` | Один раз на файл | Дорогостоящие ресурсы |
| `session` | Один раз на весь прогон | БД, браузер, API |

### Когда использовать ✅

- Дорогостоящая настройка (БД, браузер, API)
- Одинаковые сложные данные в 10+ тестах
- Автоматическая очистка ресурсов

### Когда НЕ использовать ❌

- Простые данные (числа, строки) — пиши явно в тесте
- Когда фикстура скрывает смысл теста

---

## 🎯 ПАРАМЕТРИЗАЦИЯ

### Базовый синтаксис

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (10, 5, 15),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

### Параметризация исключений

```python
@pytest.mark.parametrize("a,b", [
    (10, 0),
    (5, 0),
])
def test_divide_by_zero(a, b):
    with pytest.raises(ZeroDivisionError):
        divide(a, b)
```

### Комбинация параметризаций

```python
@pytest.mark.parametrize("a", [1, 2, 3])
@pytest.mark.parametrize("b", [10, 20])
def test_multiply(a, b):  # 6 прогонов: 3×2
    assert multiply(a, b) == a * b
```

### С фикстурами

```python
@pytest.mark.parametrize("a,b,expected", [
    (10, 5, 15),
])
def test_add_with_fixture(a, b, expected, calc):
    result = calc.add(a, b)
    assert result == expected
```

---

## 📁 CONFTEST.PY

### Что это

Специальный файл — фикстуры доступны во всех тестах без импорта.

### Структура

```python
# tests/conftest.py
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
))

from src.calculator import add, divide

@pytest.fixture
def numbers():
    return {"a": 10, "b": 5}
```

### Иерархия

```
tests/
├── conftest.py          # для всех тестов
├── api/conftest.py      # только для api/
└── ui/conftest.py       # только для ui/
```

### autouse=True

```python
@pytest.fixture(autouse=True)
def log_test():
    print("Тест начался")
    yield
    print("Тест завершился")
```

**Использовать для:** логирования, очистки ресурсов  
**Не использовать для:** тестовых данных, моков

---

## 🏷️ МАРКЕРЫ И СЕЛЕКТИВНЫЙ ЗАПУСК

### Встроенные маркеры

```python
@pytest.mark.skip(reason="Не готово")
def test_future(): ...

@pytest.mark.skipif(sys.platform == "win32", reason="Linux only")
def test_linux(): ...

@pytest.mark.xfail(reason="Баг #123")
def test_buggy(): ...
```

### Свои маркеры

```ini
# pytest.ini
[pytest]
markers =
    api: тесты API
    smoke: дымовые тесты
    slow: медленные тесты
```

```python
@pytest.mark.smoke
@pytest.mark.api
def test_add():
    assert add(2, 3) == 5
```

### Запуск

```cmd
pytest -m smoke              # только smoke
pytest -m "not slow"         # всё кроме slow
pytest -m "api and not slow" # комбинация
pytest -k "add"              # по имени
pytest -m api -k "divide"    # маркер + имя
```

### Отчёты с фильтрацией

```cmd
pytest -m smoke --html=reports/smoke.html
pytest -m "not slow" --junitxml=ci-results.xml
```

---

## 🗣️ ДЛЯ СОБЕСА

**Что такое фикстуры?**

Функции для подготовки окружения тестов. Позволяют вынести setup/teardown в одно место, переиспользовать код и гарантировать очистку даже при падении теста.

**Что такое conftest.py?**

Специальный файл, где объявленные фикстуры автоматически доступны во всех тестах без импорта.

**Зачем нужна параметризация?**

Один тест — много данных. Сокращает код, покрывает больше сценариев, легче поддерживать.

**Почему pytest лучше unittest?**

Меньше бойлерплейта, читаемый синтаксис (`assert`), фикстуры вместо `setUp/tearDown`, параметризация, 1000+ плагинов, умные ошибки. Совместим с unittest.

**Что такое autouse=True?**

Фикстура выполняется автоматически в каждом тесте. Для логирования, очистки ресурсов.

**Встроенные фикстуры?**

`tmp_path` (временная папка), `capfd` (перехват print), `caplog` (логи), `monkeypatch` (моки ENV).

---

## ❓ ВОПРОСЫ ДЛЯ САМОПРОВЕРКИ

1. Чем `pytest -v` отличается от `pytest -s`?
2. Зачем нужен `yield` в фикстуре?
3. Как параметризовать тест с исключением?
4. Что такое conftest.py и чем отличается от импорта?
5. Как запустить только тесты с маркером `api`?
6. Когда использовать autouse, а когда нет?
7. Как скомбинировать маркер и фильтр по имени?
8. Что покажет `pytest -k "add and not zero"`?
9. Чем `tmp_path` лучше `tempfile`?
10. Как создать фикстуру на всю сессию?

---

## 🔗 ССЫЛКИ

- [pytest документация](https://docs.pytest.org)
- [Parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [Fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.html)
- [conftest.py](https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files)
- [Markers](https://docs.pytest.org/en/stable/how-to/mark.html)
- [unittest docs](https://docs.python.org/3/library/unittest.html)
- [Git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)

---

## 📝 ЛИЧНЫЕ ЗАМЕТКИ

### Инсайты



### Ошибки и решения



### Вопросы для ментора



### Время затрачено

- Всего: __ часов

---

## ✅ ЧЕК-ЛИСТ НЕДЕЛИ 2

- [ ] Понимаю разницу unittest vs pytest
- [ ] Знаю конвенции pytest (именование, запуск)
- [ ] Понимаю фикстуры и когда использовать
- [ ] Создал conftest.py с фикстурами
- [ ] Использовал @pytest.mark.parametrize
- [ ] Параметризовал тесты с исключениями
- [ ] Знаю встроенные фикстуры (tmp_path, capfd)
- [ ] Настроил pytest.ini с маркерами
- [ ] Могу запустить по маркеру: `pytest -m api`
- [ ] Могу запустить по имени: `pytest -k "add"`
- [ ] Знаю что такое autouse=True
- [ ] Понимаю иерархию conftest
- [ ] Могу объяснить различия на собесе