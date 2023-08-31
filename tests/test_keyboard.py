import pytest

from src.keyboard import Keyboard


@pytest.fixture()
def test_keyboard():
    return Keyboard("Dark Project KD87A", 9500, 5)


def test_init(test_keyboard):
    assert str(test_keyboard) == "Dark Project KD87A"


def test_language(test_keyboard):
    assert test_keyboard.language == "EN"


def test_change_lang(test_keyboard):
    test_keyboard.change_lang()
    assert test_keyboard.language == "RU"
    test_keyboard.change_lang()
    assert test_keyboard.language == "EN"


def test_error_set_language(test_keyboard):
    with pytest.raises(AssertionError):
        test_keyboard.language = "FR"

