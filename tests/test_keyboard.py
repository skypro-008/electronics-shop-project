""" Keyboard class testing module """
import pytest


def test_keyboard_properties(keyboard):
    """
    Test the properties of a keyboard.

    Args:
        keyboard (Keyboard): The keyboard object to test.
    """
    assert keyboard.name == 'Keyboard'
    assert keyboard.price == 10.0
    assert keyboard.quantity == 5


def test_keyboard_change_language(keyboard):
    """
    Test the change_lang method of a keyboard.

    Args:
        keyboard (KeyBoard): The keyboard object to test.
    """
    assert keyboard.language == 'EN'

    keyboard.change_lang()
    assert keyboard.language == 'RU'

    keyboard.change_lang()
    assert keyboard.language == 'EN'


def test_keyboard_add_language(keyboard):
    """
    Test adding a language to the keyboard.

    Attempts to assign a new language to the keyboard using the
    `language` attribute.

    Expects an AttributeError to be raised.

    Args:
        keyboard (KeyBoard): The keyboard object to test.
    """

    with pytest.raises(AttributeError):
        keyboard.language = 'GE'
