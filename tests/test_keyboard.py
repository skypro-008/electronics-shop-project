from src.keyboard import Keyboard
import pytest


@pytest.fixture
def test_keyboard():
    return Keyboard("NiceKeyboard", 1000, 5)


def test_change_lang(kb):
    '''Тестируем переключение языка'''
    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали EN -> RU -> EN
    kb.change_lang().change_lang().change_lang()
    assert str(kb.language) == "EN"
