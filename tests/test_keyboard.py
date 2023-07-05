
import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard_test():
    return Keyboard('Клавиатура', 9600, 5)


def test_change_lang(keyboard_test):
    assert keyboard_test.language == "EN"
    keyboard_test.change_lang()
    assert keyboard_test.language == "RU"
    keyboard_test.change_lang()
    assert keyboard_test.language == "EN"
