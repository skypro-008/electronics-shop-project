"""Тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone


def test_item():
    item = Item("Телевизор", 100_000, 3)
    assert item.name == "Телевизор"
    assert item.price == 100_000
    assert item.quantity == 3


def test_calculate_total_price():
    item = Item("Телевизор", 100_000, 3)
    assert item.calculate_total_price() == 300_000


def test_apply_discount():
    item = Item("Телевизор", 100_000, 3)
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 50_000


def test__add__():
    item1 = Item("Телевизор", 100_000, 6)
    phone1 = Phone("Sumsung", 100_000, 3, 1)
    assert item1 + phone1 == 9
    assert phone1 + phone1 == 6
