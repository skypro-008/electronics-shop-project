from src.item import Item
from src.phone import Phone

import pytest
@pytest.fixture()
def phone1():
    return Phone("iPhone 14", 120000, 5, 2)

@pytest.fixture()
def item2():
    return Item("Ноутбук", 20000, 5)

def test_str(phone1):
    """
    Тестирует метод str
    """
    assert str(phone1) == 'iPhone 14'

def test_repr(phone1):
    """
    Тестирует метод repr
    """
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test_number_of_sim(phone1):
    assert phone1.number_of_sim == 2

# def test_number_of_sim0(phone1):
#     phone1.number_of_sim = 0
#     assert ValueError

def test_add(item2, phone1):
    assert item2 + phone1 == 10
    assert phone1 + phone1 == 10


