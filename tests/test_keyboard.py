from src.keyboard import Keyboard
import pytest

kb = Keyboard('Dark Project KD87A', 9600, 5)
assert str(kb) == "Dark Project KD87A"

def __language_test():
    """Проверяет ошибку"""
    with pytest.raises(AttributeError):
        kb.__language = 'CH'

def test_language():
    """Проверяет изначальную раскладку клавиатуры"""
    assert str(kb.language) == "EN"

def test_change_lang():
    """Проверяет метод смены языка"""
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"


