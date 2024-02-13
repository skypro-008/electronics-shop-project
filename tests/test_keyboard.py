from src.keyboard import Keyboard
from src.item import Item
import pytest

@pytest.fixture()
def keyboard_example():
    return Keyboard("Acer X2-00", 5000, 20)

def test_str(keyboard_example):
    assert str(keyboard_example) == "Acer X2-00"

def test_language(keyboard_example):
    assert keyboard_example.language == 'EN'

def test_change_lang(keyboard_example):
    keyboard_example.change_lang()
    assert keyboard_example.language == 'RU'

