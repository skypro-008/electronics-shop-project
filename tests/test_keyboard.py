import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import KeyBoard


def test_init():
    keyboard = KeyBoard('Logitech Wireless MX Keys Mini', 1600, 10)
    assert str(keyboard) == "Logitech Wireless MX Keys Mini"
    assert keyboard.price == 1600
    assert keyboard.quantity == 10

def test_change_lang():
    keyboard = KeyBoard('Logitech Wireless MX Keys Mini', 1600, 10)
    assert str(keyboard.language) == 'EN'
    keyboard.change_lang()
    assert str(keyboard.language) == 'RU'
    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == 'RU'

def test_error_setter_language():
    keyboard = KeyBoard('Logitech Wireless MX Keys Mini', 1600, 10)
    with pytest.raises(AttributeError):
        keyboard.lang = 'CH'
