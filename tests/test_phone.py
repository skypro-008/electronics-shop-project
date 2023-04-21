import pytest
from src.item import Item
from src.phone import Phone


def test___radd__():
    phone1 = Phone("iPhone 14", 100000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert phone1 + phone1 == 10
    assert item1 + phone1 == 25


def test__str__():
    phone1 = Phone("iPhone 14", 100000, 5, 2)
    assert str(phone1) == "iPhone 14"


def test__repr__():
    phone1 = Phone("iPhone 14", 100000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 100000, 5, 2)"