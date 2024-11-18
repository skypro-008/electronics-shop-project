from src.item import Item
from src.keyboard import Keyboard
import pytest


def test_keyboard():
    kb = Keyboard('some', 9600, 5)
    assert str(kb) == "some"

    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb._language) == "RU"
    kb.change_lang()
    assert str(kb._language) == "EN"
    kb.change_lang()
    assert str(kb._language) == "RU"
    kb.change_lang()
    assert str(kb._language) == "EN"
