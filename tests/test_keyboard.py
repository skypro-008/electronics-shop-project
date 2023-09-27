import pytest

from src.keyboard import Keyboard, MixinLang


@pytest.fixture
def kb1_test():
    return Keyboard("Клавиатура - 34", 103, 15)


@pytest.fixture
def kb2_test():
    return Keyboard("Клавиатура Наименование товара не более 10 символов", 103, 15)


def test_init(kb1_test):
    assert kb1_test.name == "Клавиатура"
    assert kb1_test.price == 103
    assert kb1_test.language == "EN"


def test_change_lang(kb1_test, kb2_test):
    assert kb1_test.language == "EN"
    assert kb2_test.language == "EN"
    kb1_test.change_lang()
    assert kb1_test.language == "RU"
    assert kb2_test.language == "EN"
    kb1_test.change_lang()
    kb2_test.change_lang()
    assert kb1_test.language == "EN"
    assert kb2_test.language == "RU"
