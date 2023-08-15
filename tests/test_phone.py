import pytest
from src.phone import Phone
from src.item import Item

phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_str():
    assert str(phone1) == 'iPhone 14'
    assert str(phone1) != 'iPhone 13'


def test_repr():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert repr(phone1) != "figna"


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
