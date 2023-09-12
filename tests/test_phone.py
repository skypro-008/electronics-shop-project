import pytest

from src.item import Item
from src.phone import Phone


def test_add_item_and_phone():
    item1 = Item('Кабель',10,5)
    phone1 = Phone('Смартфон', 100, 1, 4)
    assert item1 + phone1 == 6
    assert phone1 + phone1 == 2
    assert item1 + item1 == 10

def test_repr():
    phone1 = Phone('Смартфон', 100, 1, 4)
    assert repr(phone1) == "Phone('Смартфон', 100, 1, 4)"

def test_str():
    phone1 = Phone('Смартфон', 100, 1, 4)
    phone2 = Phone('iPhone 14', 120_000, 5, 2)
    phone3 = Phone('Samsumg', 120_000, 5, 2)
    assert str(phone1) == 'Смартфон'
    assert str(phone2) == 'iPhone 14'
    assert str(phone3) == 'Samsumg'
