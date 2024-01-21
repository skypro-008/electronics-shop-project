from src.keyboard import *
import pytest


@pytest.fixture
def keyboard():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    return keyboard


def test___repr__(keyboard):
    assert repr(keyboard) == "Keyboard('Dark Project KD87A', 9600, 5)"


def test___str__(keyboard):
    assert str(keyboard) == 'Dark Project KD87A'


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == 'RU'


def test_language(keyboard):
    with pytest.raises(AttributeError):
        keyboard.language = 'CH'
