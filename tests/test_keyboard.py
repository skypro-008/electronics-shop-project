import pytest


def test_init(test_keyboard):
    assert test_keyboard.name == 'Oklick 760G GENESIS'
    assert test_keyboard.price == 1400
    assert test_keyboard.quantity == 30
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

