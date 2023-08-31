import pytest

from src.keyboard import Keyboard


@pytest.fixture
def keyboard_data():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    return keyboard

def test_keyboard_init(keyboard_data):
    assert str(keyboard_data) == "Dark Project KD87A"
    assert keyboard_data.price == 9600
    assert keyboard_data.quantity == 5
    assert str(keyboard_data.language) == "EN"

def test_keyboard_change_lang(keyboard_data):
    keyboard_data.change_lang()
    assert str(keyboard_data.language) == "RU"

    keyboard_data.change_lang().change_lang()
    assert str(keyboard_data.language) == "RU"