from src.keyboard import Keyboard


def test_add():
    kb = Keyboard('Sly', 50000, 30)
    assert kb.quantity == 30
    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"

