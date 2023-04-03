import pytest
from src.keyboard import KeyBoard


@pytest.fixture
def test_data_one():
    return 'Dark Project KD87A', 9600, 5


def test_keyboard(test_data_one):
    kl = KeyBoard(*test_data_one)
    assert str(kl) == "Dark Project KD87A"
    assert str(kl.language) == "EN"
    kl.change_lang()
    assert str(kl.language) == "RU"
    kl.change_lang()
    assert str(kl.language) == "EN"
