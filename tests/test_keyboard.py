from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_init():
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.price) == '9600'
    assert str(kb.quantity) == '5'
    assert str(kb.language) == "EN"


def test_change_lang():
    kb.change_lang()
    assert str(kb.language) == "RU"
    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"
