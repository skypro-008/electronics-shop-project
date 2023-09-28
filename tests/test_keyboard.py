from src.keyboard import Keyboard

def test_repr():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert repr(kb) == "Keyboard('Dark Project KD87A', 9600, 5, EN)"


def test_str():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"