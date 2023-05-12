from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_str():
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"


def test_change_lang():
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

