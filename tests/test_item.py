"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item

def test_calculate_total_price():
    item1 = Item("Смартфон", 50000, 30)
    item2 = Item("Ноутбук", 80000, 20)

    assert item1.calculate_total_price() == 1500000
    assert item2.calculate_total_price() == 1600000

def test_apply_discount():
    item1 = Item("Смартфон", 50000, 30)
    item2 = Item("Ноутбук", 80000, 20)


    assert item1.price == 50000
    assert item2.price == 80000

    Item.pay_rate = 0.8

    item1.apply_discount()

    assert item1.price == 40000
    assert item2.price == 80000

