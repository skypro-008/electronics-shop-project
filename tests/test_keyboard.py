import pytest
from src.keyboard import Keyboard


@pytest.fixture
def cls_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_change_lang(cls_keyboard):
    assert cls_keyboard.language == "EN"
    cls_keyboard.change_lang()
    assert cls_keyboard.language == "RU"
    cls_keyboard.change_lang().change_lang()
    assert cls_keyboard.language == "RU"
    cls_keyboard.change_lang().change_lang().change_lang()
    assert cls_keyboard.language == "EN"
