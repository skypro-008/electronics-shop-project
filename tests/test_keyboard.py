import pytest

from src.keyboard import Keyboard


def test_change_language():
    """
    Тест для метода change_language
    """

    kb1 = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb1.language == "EN"

    kb1.change_lang()
    assert kb1.language == "RU"

    kb1.change_lang().change_lang()
    assert kb1.language == "RU"
