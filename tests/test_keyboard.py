import pytest

from src.keyboard import Keyboard


@pytest.fixture()
def keyboard():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb

@pytest.fixture()
def mixin():
    lang = "EN"
    return lang

def test_init(keyboard):
    assert keyboard.name == 'Dark Project KD87A'
    assert keyboard.price == 9600
    assert keyboard.quantity == 5

def test_change_lang(keyboard):
    assert str(keyboard.language) == "EN"
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"
    keyboard.change_lang()
    assert str(keyboard.language) == "EN"