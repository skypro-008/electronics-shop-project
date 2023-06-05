import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import KeyBoard


def test_init(test_keyboard):
    assert test_keyboard.name == 'Logitech Wireless MX Keys Mini (920-010501)'
    assert test_keyboard.price == 1600
    assert test_keyboard.quantity == 10
    assert test_keyboard.language == 'EN'
    with pytest.raises(AttributeError):
        test_keyboard.language = 'RU'


def test_change_lang(test_keyboard):
    test_keyboard.change_lang()
    assert test_keyboard.language == 'RU'
    test_keyboard.change_lang()
    assert test_keyboard.language == 'EN'
    test_keyboard.change_lang().change_lang()
    assert test_keyboard.language == 'EN'

