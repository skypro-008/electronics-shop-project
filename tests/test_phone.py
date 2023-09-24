"""Тесты с использованием pytest для модуля Phone"""
import pytest

from src.item import Item
from src.phone import Phone

@pytest.fixture
def phone_test1():
    return Phone("Аврора", 100000, 1, 5)
@pytest.fixture
def phone_test2():
    return Phone("1234567890----", 100, 100, 1)

def test_phone_init(phone_test1, phone_test2):
    ''' тест конструктора'''

    assert phone_test1.name == "Аврора"
    assert phone_test1.price == 100000.0
    assert phone_test1.quantity == 1
    assert phone_test1.number_of_sim == 5
    assert phone_test2.name == '1234567890'
    try:
        Phone("Мяо", 10000, 1000, 0)
    except Exception as e:
        assert e

def test_phone_add(phone_test1, phone_test2):

    assert phone_test1 + phone_test2 == 101


