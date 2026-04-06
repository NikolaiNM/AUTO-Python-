# test_scopes.py
import pytest


# 🔹 function (по умолчанию) - создаётся для КАЖДОГО теста
@pytest.fixture
def func_fixture():
    print("\n  [function] SETUP")
    yield "func"
    print("  [function] TEARDOWN")


# 🔹 class - один раз на весь класс тестов
@pytest.fixture(scope="class")
def class_fixture():
    print("\n  [class] SETUP")
    yield "class"
    print("  [class] TEARDOWN")


# 🔹 module - один раз на весь файл
@pytest.fixture(scope="module")
def module_fixture():
    print("\n  [module] SETUP")
    yield "module"
    print("  [module] TEARDOWN")


# 🔹 session - один раз на все тесты
@pytest.fixture(scope="session")
def session_fixture():
    print("\n  [session] SETUP")
    yield "session"
    print("  [session] TEARDOWN")


class TestScopes:
    def test_1(self, func_fixture, class_fixture, module_fixture, session_fixture):
        print("  🧪 Test 1 running")
        assert True

    def test_2(self, func_fixture, class_fixture, module_fixture, session_fixture):
        print("  🧪 Test 2 running")
        assert True

    def test_3(self, func_fixture, class_fixture, module_fixture, session_fixture):
        print("  🧪 Test 3 running")
        assert True