"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_class_item():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000
    assert item1.apply_discount() == 8000
