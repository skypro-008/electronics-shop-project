import pytest

from src.keyboard import Keyboard


def test():
    """
    проверка смены языковой раскладки клавиатуры
    """
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
