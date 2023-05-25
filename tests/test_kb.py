from src.keyboard import Keyboard


def test_kb():
    kb = Keyboard(name='Name', price=2, quantity=3)
    assert kb.language == 'EN'
    kb.change_lang()
    assert kb.language == 'RU'
    kb.change_lang().change_lang()
    assert kb.language == 'RU'