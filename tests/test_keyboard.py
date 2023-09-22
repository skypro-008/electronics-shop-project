from src.keyboard import Keyboard


def test_language_keyboard():
    keyboard = Keyboard('',0,1)
    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'
