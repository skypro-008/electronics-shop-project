import pytest
from src.keyboard import KeyBoard


@pytest.fixture
def keyboard1():
    return KeyBoard('Ducky One 3', 15000, 9)


def test_init(keyboard1):
    assert keyboard1.name == 'Ducky One 3'
    assert keyboard1.price == 15000
    assert keyboard1.quantity == 9
    assert keyboard1.language == 'EN'


def test_change_lang(keyboard1):
    keyboard1.change_lang()
    assert keyboard1.language == 'RU'

    keyboard1.change_lang()
    assert keyboard1.language == 'EN'