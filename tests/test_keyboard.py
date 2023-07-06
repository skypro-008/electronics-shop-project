import pytest

from src.keyboard import Keyboard

def test_change_lang():
    kb = Keyboard('Dark Project', 9600, 5)
    assert str(kb) == "Dark Project"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"


    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

def test_erorr():
    kb = Keyboard('Dark Project', 9600, 5)
    with pytest.raises(AttributeError):
        kb.language = 'CH'


