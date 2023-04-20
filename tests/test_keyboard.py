import pytest

from src.keyboard import KeyBoard
from src.keyboard import MixinKeyLang


@pytest.fixture
def return_date():
    """Описание фикстуры для тестов"""
    return KeyBoard("Чайник", 10000, 20)


def test_init(return_date):
    """Тест для init, класс KeyBoard"""
    assert return_date.price == 10000
    assert return_date.name == 'Чайник'
    assert return_date.quantity == 20


def test_mixin_key_lang():
    """Тест для миксин- класса MixinKeyLang"""
    mixin_key_lang = MixinKeyLang()
    assert mixin_key_lang.language == "EN"
    mixin_key_lang.change_lang()
    assert mixin_key_lang.language == "RU"
    mixin_key_lang.change_lang()
    assert mixin_key_lang.language == "EN"
    with pytest.raises(AttributeError):
        mixin_key_lang.language = "Mumba Yumba"
