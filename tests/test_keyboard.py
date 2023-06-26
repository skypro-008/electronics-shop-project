import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard1():
    return Keyboard('Logitech', 10000, 5)


def test_keyboard_init(keyboard1):
    assert keyboard1.name == 'Logitech'
    assert keyboard1.price == 10000
    assert keyboard1.quantity == 5
    assert keyboard1.language == 'EN'


def test_keyboard_change_lang(keyboard1):
    keyboard1.change_lang()
    assert str(keyboard1.language) == "RU"
