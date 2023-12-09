from src.keyboard import Keyboard

kb = Keyboard("Sample Keyboard", 500, 10)


def test_keyboard_init():
    assert kb.name == "Sample Keyboard"
    assert kb.price == 500
    assert kb.quantity == 10
    assert kb.language == 'EN'


def test_language():
    kb.change_lang()
    assert str(kb.language) == 'RU'


def test_change_lang():
    assert str(kb.language) == 'EN'


def test_other_language():
    assert str(kb.language) != 'CH'
