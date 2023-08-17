"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


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