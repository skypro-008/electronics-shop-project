from src.Keyboard import Keyboard


def test_keyboard_language():
    kb = Keyboard('model', 9600, 104)
    assert kb.language == 'EN'

    kb.language = 'RU'
    assert kb.language == 'RU'

    kb.change_lang()
    assert kb.language == 'EN'