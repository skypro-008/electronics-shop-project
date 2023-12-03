import pytest

from src.keyboard import Keyboard


@pytest.fixture
def keybord_fixture():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb


def test__str__(keybord_fixture):
    kb = keybord_fixture
    assert str(kb) == "Dark Project KD87A"


def test_change_lang(keybord_fixture):
    kb = keybord_fixture
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"
