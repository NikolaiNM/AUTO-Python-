# 🐍 Python Automation QA

Мой учебный проект по изучению автоматизации тестирования на Python

## О проект

Этот репозиторий создан для самостоятельного обучения Python

## Требования
- Python 3.14+
- pip 
- git

## Запуск

```bash
# 1. Клонировать репозиторий

# 2. Создать виртуальное окуржения 
python -m venv venv

# 3. Активировать виртуальное окружение
# Windows:
venv\scripts\activate 
# macOS/Linux:
source venv/bin/activate

# 4. Установить зависимости
pip install -r requiremenrs.txt
```

### Запуск тестов
```bash
# Все тесты
pytest

# Подробный вывод
pytest -v

# Тесты с отчетом в HTML
pytest --html=report.html

# Конкретный файл
pytest tests/test_calculator.py -v

# Конкретный тест
pytest tests/test_calculator.py::TestDivide::test_divide_positive -v
```