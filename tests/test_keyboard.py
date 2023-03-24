
import pytest
from src.keyboard import Keyboard

@pytest.fixture
def item_keyboard():
    return Keyboard("keyboard", 10000, 5)

def test_lang(item_keyboard):
    assert item_keyboard.language == "EN"

def test_change_lang(item_keyboard):
    item_keyboard.change_lang()
    assert item_keyboard.language == "RU"