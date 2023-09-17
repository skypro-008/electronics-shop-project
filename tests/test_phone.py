import pytest
from src.item import Item
from src.phone import Phone

def test__add__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert phone1 + item1 == 25
    assert item1 + item1 == 40