from src.keyboard import Keyboard


def test__str__():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert kb.language == "EN"


def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert kb.language == 'RU'
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang().change_lang()
    assert kb.language == 'EN'
