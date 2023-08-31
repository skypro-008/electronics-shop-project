import pytest

from src.item import Item
from src.phone import Phone


def test_init():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
        phone1.number_of_sim = 2.5

def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 10, 2)
    item4 = Item("Смартфон", 10000, 20)
    assert item4 + phone1 == 30
    with pytest.raises(ValueError):
        phone1 + 'item4'
        phone1 + 1234


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 10, 2)
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
        phone1.number_of_sim = 2.5
