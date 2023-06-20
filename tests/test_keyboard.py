from src.keyboard import Keyboard

def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert  kb.change_lang().change_lang().language == "EN"
    assert  kb.change_lang().language == "RU"