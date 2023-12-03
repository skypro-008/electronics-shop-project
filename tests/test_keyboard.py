import pytest
from random import randint
from src.keyboard import *


def test_Keyboard_language():
    item = Keyboard("Dark Project KD87A", randint(10000, 100000), randint(1, 100))
    assert item.language == 'EN'

def test_change_lang():
    item = Keyboard('Razer', randint(10000, 100000), randint(1, 100))
    item.change_lang()
    assert item.language == 'RU'