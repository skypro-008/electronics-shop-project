from src.keyboard import Keyboard
kb = Keyboard("name", 1, 2)

def test_init():
    assert kb.name == "name"
    assert kb.price == 1
    assert kb.quantity == 2
    assert kb.language == "EN"

def test_change_lang():
    kb.change_lang()
    assert kb.language == "RU"
    lang_setter = False
    try:
        kb.language = "CH"
        lang_setter = True
    except AttributeError:
        pass
    assert lang_setter == False