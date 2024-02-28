import pytest
from config import root_csv
from src.keyboard import Keyboard

@pytest.fixture
def example():
    return(Keyboard("a4tech kv-300h", 10000, 20))

def test_Keyboard(example):
    assert str(example) == "a4tech kv-300h"
    assert str(example.language) == "EN"

    example.change_lang()
    assert str(example.language) == "RU"

    example.change_lang()
    assert str(example.language) == "EN"

    with pytest.raises(AttributeError):
        example.language = 'CH'