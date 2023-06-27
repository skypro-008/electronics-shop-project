import pytest

from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard

@pytest.fixture
def test_item():
    return Item("test_PC", 35000, 4)

@pytest.fixture
def test_phone():
    return Phone("test_ph14", 135000, 4, 2)

@pytest.fixture
def test_keyboard():
    return Keyboard("test_keyb", 5000, 9)
