import pytest

from src.keyboard import Keyboard

def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang()
    assert str(kb.language) == "EN"

def test_error():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    e = 'AttributeError'
    with pytest.raises(Exception) as e:
        kb.language = 'CH'

