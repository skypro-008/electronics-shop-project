import pytest
from src.keyboard import Keyboard


@pytest.fixture
def kb():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb


def test__init__(kb):
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5


def test_language(kb):
    assert str(kb.language) == "EN"


def test_change_lang(kb):
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"