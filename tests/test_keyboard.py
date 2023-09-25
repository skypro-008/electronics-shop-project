# -*- coding: utf-8 -*-
import pytest


def test_init(some_keyboard):
    """
    Тест инициализации
    """
    assert str(some_keyboard) == "Dark Project KD87A"
    # тест языка по-умолчанию
    assert str(some_keyboard.language) == "EN"

def test_change_lang(some_keyboard):
    """
    Тест смены языка
    """
    some_keyboard.change_lang()
    assert str(some_keyboard.language) == "RU"
    # Сделали RU -> EN -> RU
    some_keyboard.change_lang().change_lang()
    assert str(some_keyboard.language) == "RU"
    with pytest.raises(AttributeError):
        some_keyboard.language = 'CH'