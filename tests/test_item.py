"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item = Item("Смартфон", 10000, 20)
    assert(item.calculate_total_price()) == 200000


def test_apply_discount():
    item = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.9
    item.apply_discount()
    assert (item.calculate_total_price()) == 180000.0
