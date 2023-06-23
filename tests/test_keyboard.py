from src.keyboard import Keyboard


def test_key_board():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert kb.price == 9600
    assert kb.quantity == 5

    assert str(kb.language) == "EN"
    assert kb.language == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"
    assert kb.language == "RU"

    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
