from src.keyboard import Keyboard
import pytest


def test_repr(test_case_keyboard):
    assert repr(test_case_keyboard) == "Keyboard('Dark Project KD87A', 9600, 5, 'EN')"


def test_str(test_case_keyboard):
    assert str(test_case_keyboard) == "Dark Project KD87A"


def test_change_lang(test_case_keyboard):
    test_case_keyboard.change_lang()
    assert test_case_keyboard.language == "RU"

    test_case_keyboard.change_lang()
    assert test_case_keyboard.language == "EN"

    test_case_keyboard.change_lang().change_lang()
    assert test_case_keyboard.language == "EN"

    with pytest.raises(AttributeError):
        test_case_keyboard.language = "CH"
