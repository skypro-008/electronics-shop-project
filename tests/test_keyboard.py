"""Тесты с использованием pytest для модуля keyboard."""
from src.keyboard import Keyboard


def test_keyboard():
    """
    Тестирование создание экземпляра keyboard
    """
    kb1 = Keyboard('Dark', 7000, 5)
    assert str(kb1) == "Dark"
    assert str(kb1.language) == "EN"


def test_change_lang():
    """
    Тестирование на изменение языка
    """
    kb1 = Keyboard('Dark', 7000, 5)
    kb1.change_lang()
    assert str(kb1.language) == "RU"