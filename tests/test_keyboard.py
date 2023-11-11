from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)

def test_change_lang():

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert (str(kb.language)) == "RU"

def test_str():
    assert kb.__str__() == 'Dark Project KD87A'
