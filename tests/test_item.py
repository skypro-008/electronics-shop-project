"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


def test_item_init():
    item = Item("bananas", 10, 1.99)
    assert item.name == "bananas"
    assert item.price == 10
    assert item.quantity == 1.99

def test_calculate_total_price():
    item = Item("bananas", 10, 1.99)
    assert item.calculate_total_price() == 19.9

def test_apply_discount():

    item = Item("apples", 5, 2)
    item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 4.5

