"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Смартфон", 10000, 0)


def test_alculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 0


def test_apply_discount():
    assert item1.apply_discount(0.2) == 2000
    assert item1.apply_discount(0) == 0
