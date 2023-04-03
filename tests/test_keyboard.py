import pytest
from src.keyboard import KeyBoard


@pytest.fixture
def test_data_one():
    return 'Dark Project KD87A', 9600, 5


def test_keyboard(test_data_one):
    kb = KeyBoard(*test_data_one)
    assert str(kb) == 'Dark Project KD87A'
    assert str(kb.language) == 'EN'
    kb.change_lang()
    assert str(kb.language) == 'RU'
    kb.change_lang()
    assert str(kb.language) == 'EN'
