import pytest
from src import keyboard

if __name__ == '__main__':
    kb = keyboard.Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"
# def test_change_lang():
#     kb = keyboard.Keyboard('Dark Project KD87A', 9600, 5)
#     kb.change_lang()
#     assert str(kb.language) == "RU"
#
#     # Сделали RU -> EN -> RU
#     kb.change_lang().change_lang()
#     assert str(kb.language) == "RU"