import pytest

from src.item import Item
from src.phone import Phone

def test__repr__():
    assert Phone.__repr__(Phone('iPhone 14', 120000, 5, 2)) == "Phone('iPhone 14', 120000, 5, 2)"

def test__str__():
    assert str('iPhone 14') == 'iPhone 14'

def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2

def test__add__():
    phone1 = Phone('iPhone 14', 120000, 5, 2)
    item1 = Item('Смартфон', 10000, 20)
    assert phone1 + item1 == 25
    assert phone1 + phone1 == 10

