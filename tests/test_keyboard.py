from src.keyboard import Keyboard
import pytest


@pytest.fixture()
def keyboard_test():
    return Keyboard('Dark Project KD87A', 9600, 5)


# kb = Keyboard('Dark Project KD87A', 9600, 5)


def _language_test(keyboard_test):
    """Тест, проверяющий корректную ошибку"""
    with pytest.raises(AttributeError):
        keyboard_test._language = 'CH'


def test_language(keyboard_test):
    """
    Проверяет начальную раскладку клаиватуры
    """
    assert str(keyboard_test.language) == 'EN'


def test_change_lang(keyboard_test):
    """
    Тесты для проверки правлиьной работы метода смены языка
    """
    keyboard_test.change_lang()
    assert str(keyboard_test.language) == "RU"
    keyboard_test.change_lang()
    assert str(keyboard_test.language) == "EN"
