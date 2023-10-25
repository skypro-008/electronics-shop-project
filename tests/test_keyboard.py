from src.keyboard import Keyboard
import pytest


@pytest.fixture
def test_keyboard():
    return Keyboard("NiceKeyboard", 1000, 5)


