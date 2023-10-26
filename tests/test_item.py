"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


item1 = Item("Смартфон", 1000, 20)
item2 = Item("Планшет", 10000, 2)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 20000
    assert item2.calculate_total_price() == 20000


def test_apply_discount():
    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 500
    item2.apply_discount()
    assert item2.price == 5000

