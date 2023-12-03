from src.keyboard import KeyBoard


def test_add():
    kb = KeyBoard('Sly', 50000, 30)
    assert kb.quantity == 30
    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang()
    assert str(kb.language) == "EN"

