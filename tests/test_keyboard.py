import pytest

def test__init__(test_keyboard):
    assert test_keyboard.name == "test_keyb"
    assert test_keyboard.price == 5000
    assert test_keyboard.quantity == 9
    assert test_keyboard.language == "EN"
    test_keyboard.change_lang = "RU"
    assert test_keyboard.change_lang == "RU"
