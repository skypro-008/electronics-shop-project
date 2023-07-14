import pytest
from src.keyboard import Keyboard

@pytest.fixture
def test_kb1():
    return Keyboard("KB1", 100, 2)


def test_language(test_kb1):
    assert test_kb1.language == 'EN'

def test_change_lang(test_kb1):
    test_kb1.change_lang()
    assert test_kb1.language == 'RU'
    test_kb1.change_lang()
    assert test_kb1.language == 'EN'
