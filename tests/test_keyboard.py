import pytest
from src.keyboard import Keyboard


def test_keyboard_creation():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"


def test_keyboard_language_initialization():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"


def test_keyboard_change_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"


def test_keyboard_change_language_back_and_forth():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"


def test_keyboard_language_attribute_error():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    with pytest.raises(AttributeError):
        kb.language = 'CH'


if __name__ == '__main__':
    pytest.main([__file__])
