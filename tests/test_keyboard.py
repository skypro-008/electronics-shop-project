import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_creation(keyboard):
    assert keyboard.name == 'Dark Project KD87A'
    assert keyboard.price == 9600
    assert keyboard.quantity == 5
    assert keyboard.language == 'EN'


def test_keyboard_language_change(keyboard):
    assert keyboard.language == 'EN'

    keyboard.change_lang()
    assert keyboard.language == 'RU'

    keyboard.change_lang()
    assert keyboard.language == 'EN'


def test_keyboard_invalid_language(keyboard):
    with pytest.raises(ValueError):
        keyboard.language = 'CH'


def test_keyboard_string_representation(keyboard):
    assert str(keyboard) == 'Dark Project KD87A'


def test_keyboard_repr(keyboard):
    assert repr(keyboard) == "Keyboard('Dark Project KD87A', 9600, 5)"
