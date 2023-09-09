import pytest

from src.item import Item
from src.keyboard import Keyboard
from src.language_mixin import LanguageMixin


@pytest.fixture
def keyboard_fixture():
    return Keyboard("Long keyboard name", 0, 0)


def test_keyboard_name_prop(safe_item_class, keyboard_fixture):
    assert keyboard_fixture.name == "Long keyboard name"


def test_keyboard_Types(safe_item_class, keyboard_fixture):
    assert isinstance(keyboard_fixture, Item)
    assert isinstance(keyboard_fixture, LanguageMixin)
