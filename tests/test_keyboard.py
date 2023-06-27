import pytest
from src.keyboard import Keyboard


def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"