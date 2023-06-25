import pytest
from src.item import Item
"""Здесь надо написать тесты с использованием pytest для модуля item."""

test_item1 = Item("Товар1", 100, 2)
test_item2 = Item("Товар2", 50, 3)


def test_calculate_total_price():
    assert test_item1.calculate_total_price() == 200.0
    assert test_item2.calculate_total_price() == 150.0


def test_apply_discount():
    Item.pay_rate = 0.8
    test_item1.apply_discount()
    assert test_item1.price == 80.0
