import pytest
from src.keyboard import LanguageMixin


def test_init_language():
    """Тест на значение раскладки по умолчанию"""
    lm = LanguageMixin()
    assert lm._language == "EN"


def test_change_lang(keyboard_dark_project_kd87a_9600_5):
    """Тест на изменение раскладки у клавиатуры"""
    assert str(keyboard_dark_project_kd87a_9600_5) == "Dark Project KD87A"

    assert str(keyboard_dark_project_kd87a_9600_5.language) == "EN"
    keyboard_dark_project_kd87a_9600_5.change_lang()
    assert str(keyboard_dark_project_kd87a_9600_5.language) == "RU"
    keyboard_dark_project_kd87a_9600_5.change_lang().change_lang()
    assert str(keyboard_dark_project_kd87a_9600_5.language) == "RU"

    with pytest.raises(AttributeError) as excinfo:
        keyboard_dark_project_kd87a_9600_5.language = 'CH'
    assert str(excinfo.value) == "property 'language' of 'KeyBoard' object has no setter"
