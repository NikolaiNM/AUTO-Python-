# 📓 Заметки: Неделя 2 — pytest основы

## 📋 ОГЛАВЛЕНИЕ

- [pytest — база](#-pytest--база)
- [Фикстуры](#-фикстуры)
- [Параметризация](#-параметризация)
- [conftest.py](#-conftestpy)
- [Маркеры и селективный запуск](#-маркеры-и-селективный-запуск)
- [Для собеседования](#-для-собеседования)
- [Вопросы для самопроверки](#-вопросы-для-самопроверки)

---

## 🧪 PYTEST — БАЗА

### Конвенции именования

- **Файлы:** `test_*.py` или `*_test.py`
- **Функции:** `def test_*():`
- **Классы:** `class Test*` (без `__init__`)

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

### Assert vs unittest

**✅ pytest — просто:**

```python
assert add(2, 3) == 5
```

**❌ unittest — многословно:**

```python
self.assertEqual(add(2, 3), 5)
```

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

```python
@pytest.fixture(scope="session")
def browser():
    browser = Browser()
    browser.launch()
    yield browser
    browser.close()  # закроется один раз после всех тестов
```

### conftest.py

- ✅ Фикстуры доступны во всех тестах **без импорта**
- ✅ Лежит в `tests/` или подпапках
- ❌ **Не делится импортами**, только фикстурами!

### Когда использовать ✅

- Дорогостоящая настройка (БД, браузер, API)
- Одинаковые сложные данные в 10+ тестах
- Автоматическая очистка ресурсов
- Моки и заглушки

### Когда НЕ использовать ❌

- Простые данные (числа, строки) — пиши явно в тесте
- Когда фикстура скрывает смысл теста
- Когда тест становится менее читаемым

### Пример: ХОРОШО

```python
def test_add_two_positive_numbers():
    """10 + 5 = 15"""
    result = add(10, 5)
    assert result == 15
```

### Пример: ПЛОХО

```python
def test_add(self, numbers):
    result = add(numbers["a"], numbers["b"])
    assert result == 15  # ??? Какие числа?
```

---

## 🎯 ПАРАМЕТРИЗАЦИЯ

### Зачем нужна

Один тест — много данных. Сокращает код в 3-10 раз.

### Базовый синтаксис

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (10, 5, 15),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

**Что происходит:**
- Тест запустится 4 раза с разными данными
- В отчёте увидишь: `test_add[2-3-5]`, `test_add[10-5-15]`, и т.д.

### Несколько параметров

```python
@pytest.mark.parametrize("a,b,expected", [
    (10, 5, 2),
    (9, 3, 3),
    (7, 2, 3.5),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected
```

### Параметризация с фикстурами

```python
@pytest.mark.parametrize("a,b,expected", [
    (10, 5, 15),
    (0, 0, 0),
    (-5, 5, 0),
])
def test_add_with_fixture(a, b, expected, calc):
    """calc — фикстура из conftest.py"""
    result = calc.add(a, b)
    assert result == expected
```

### Когда параметризовать ✅

- Одинаковая логика, разные данные
- Пограничные значения (0, -1, None, пустая строка)
- Таблицы данных из ТЗ

### Когда НЕ параметризовать ❌

- Разная логика в каждом случае
- Когда названия тестов важнее экономии кода
- Когда параметризация делает тест нечитаемым

---

## 📁 CONFTEST.PY

### Что это

Специальный файл pytest — фикстуры из него доступны **во всех тестах** без импорта.

### Структура

```python
# tests/conftest.py
import pytest

@pytest.fixture
def numbers():
    """Тестовые данные"""
    return {"a": 10, "b": 5}

@pytest.fixture
def zero():
    return 0

@pytest.fixture
def negative():
    return -3
```

### Иерархия conftest

```
tests/
├── conftest.py          # фикстуры для всех тестов
├── api/
│   ├── conftest.py      # фикстуры только для api/
│   └── test_api.py
└── ui/
    ├── conftest.py      # фикстуры только для ui/
    └── test_ui.py
```

### autouse=True

```python
@pytest.fixture(autouse=True)
def setup_database():
    """Выполнится автоматически в каждом тесте"""
    db.connect()
    yield
    db.disconnect()
```

---

## 🏷️ МАРКЕРЫ И СЕЛЕКТИВНЫЙ ЗАПУСК

### Встроенные маркеры

```python
@pytest.mark.skip(reason="Not ready yet")
def test_not_implemented():
    pass

@pytest.mark.skipif(sys.platform == "win32", reason="Linux only")
def test_linux_only():
    pass

@pytest.mark.xfail(reason="Known bug")
def test_expected_to_fail():
    assert False
```

### Свои маркеры

```python
# tests/test_api.py

@pytest.mark.api
def test_get_users():
    pass

@pytest.mark.smoke
def test_login():
    pass

@pytest.mark.slow
def test_large_dataset():
    pass
```

### Запуск по маркеру

```cmd
pytest -m api           # только API тесты
pytest -m smoke         # только smoke тесты
pytest -m "not slow"    # все кроме slow
pytest -m "api and not slow"  # комбинация
```

### Запуск по имени

```cmd
pytest -k "add"         # все тесты с "add" в имени
pytest -k "add or multiply"
pytest -k "not divide"
```

---

## ️ ВСТРОЕННЫЕ ФИКСТУРЫ

| Фикстура | Что даёт | Пример |
|----------|---------|--------|
| `tmp_path` | Временная папка (авто-очистка) | `def test_file(tmp_path):` |
| `tmp_path_factory` | Фабрика временных папок | scope=session |
| `capfd` | Перехват print() | `captured = capfd.readouterr()` |
| `caplog` | Перехват логов | `caplog.at_level(logging.WARNING)` |
| `monkeypatch` | Мокирование ENV | `monkeypatch.setenv("KEY", "value")` |

### Пример: capfd

```python
def test_print_output(capfd):
    print("Hello from test!")
    captured = capfd.readouterr()
    assert "Hello from test!" in captured.out
```

### Пример: tmp_path

```python
def test_write_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello")
    assert file.read_text() == "Hello"
    # Папка удалится автоматически
```

---

## 🗣️ ДЛЯ СОБЕСА

**Что такое фикстуры?**

Функции для подготовки окружения тестов. Позволяют вынести setup/teardown в одно место, переиспользовать код и гарантировать очистку даже при падении теста.

**Что такое conftest.py?**

Специальный файл, где объявленные фикстуры автоматически доступны во всех тестах без импорта.

**Какие scope у фикстур?**

function (каждый тест), class (на класс), module (на файл), session (на весь прогон).

**Зачем нужна параметризация?**

Один тест — много данных. Сокращает код, покрывает больше сценариев, легче поддерживать.

**Что такое маркеры?**

Теги для группировки тестов. Позволяют запускать выборочно: `pytest -m api`.

**Встроенные фикстуры?**

`tmp_path` (временная папка), `capfd` (перехват print), `caplog` (логи), `monkeypatch` (моки ENV).

---

## ❓ ВОПРОСЫ ДЛЯ САМОПРОВЕРКИ

1. Чем `pytest -v` отличается от `pytest -s`?
2. Зачем нужен `yield` в фикстуре?
3. Что такое `conftest.py` и чем отличается от обычного импорта?
4. Как запустить только тесты с маркером `api`?
5. Когда использовать параметризацию, а когда отдельные тесты?
6. Что выполнится после `yield`, если тест упал?
7. Как создать фикстуру, которая выполнится один раз на все тесты?
8. Чем `tmp_path` лучше `tempfile`?

---

## 🔗 ССЫЛКИ

- [pytest документация](https://docs.pytest.org)
- [Fixtures guide](https://docs.pytest.org/en/stable/explanation/fixtures.html)
- [Parametrize docs](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [conftest.py docs](https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files)
- [Markers docs](https://docs.pytest.org/en/stable/how-to/mark.html)

---

## 📝 ЛИЧНЫЕ ЗАМЕТКИ

### Инсайты



### Ошибки и решения



### Вопросы для ментора



### Время затрачено

- Всего: __ часов

---

## ✅ ЧЕК-ЛИСТ НЕДЕЛИ 2

- [ ] Понимаю конвенции pytest (именование, запуск)
- [ ] Понимаю фикстуры и когда использовать
- [ ] Создал `conftest.py` с фикстурами
- [ ] Использовал `@pytest.mark.parametrize`
- [ ] Знаю встроенные фикстуры (tmp_path, capfd, monkeypatch)
- [ ] Могу запустить тесты по маркеру (`pytest -m api`)
- [ ] Могу запустить тесты по имени (`pytest -k "add"`)
- [ ] Тесты читаются как документация (явные данные)

---
