import pytest
from src.item import Item
from src.keyboard import Keyboard


@pytest.fixture
def make_items():
    kb1 = Keyboard("Keyboard 1", 10000, 20)
    kb2 = Keyboard("Keyboard 2", 20000, 5)
    return kb1, kb2


def test_keyboard(make_items):
    kb1 = make_items[0]
    kb2 = make_items[1]
    assert isinstance(kb1, Keyboard)
    assert isinstance(kb2, Item)
    assert issubclass(Keyboard, Item)


def test_change_lang(make_items):
    kb1 = make_items[0]
    kb2 = make_items[1]
    assert kb2.language == 'EN'
    kb1.change_lang()
    assert kb1.language == 'RU'


def test_keyboard(make_items):
    kb1 = make_items[0]
    assert kb1.language == 'EN'
