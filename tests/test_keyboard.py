import pytest

from src.item import Item
from src.keyboard import Keyboard


def test_keyboard_creation():
    k = Keyboard("Logitech G502", 59.99, 10)
    assert isinstance(k, Keyboard)
    assert isinstance(k, Item)
    assert k.name == "Logitech G502"
    assert k.price == 59.99
    assert k.quantity == 10


def test_default_language():
    k = Keyboard("Logitech G502", 59.99, 10)
    assert k.language == "EN"


def test_language_change():
    k = Keyboard("Logitech G502", 59.99, 10)
    k.change_lang()
    assert k.language == "RU"
    k.change_lang()
    assert k.language == "EN"