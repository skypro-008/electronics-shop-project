from src.keyboard import KeyBoard


def test_init():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5


def test_change_lang():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert kb.change_lang == 'EN'
