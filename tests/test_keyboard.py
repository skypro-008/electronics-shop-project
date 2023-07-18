import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard("Samsung", 1000, 5)


def test_lang(keyboard):
    assert keyboard.language == "EN"


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == 'RU'
