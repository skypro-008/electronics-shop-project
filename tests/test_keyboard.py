from src.keyboard import Keyboard


def test_keyboard_init():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.name == "Dark Project KD87A"
    assert kb.price == 9600
    assert kb.quantity == 5


def test_change_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"
