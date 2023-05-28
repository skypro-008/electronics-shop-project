"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src import item


def test_calculate_total_price():
    assert item.Item("Смартфон", 10000, 20).calculate_total_price() == 200000
    assert item.Item("Ноутбук", 20000, 5).calculate_total_price() == 100000

def test_apply_discount():

    testItem = item.Item("Смартфон", 10000, 20)
    item.Item.pay_rate = 0.3
    testItem.apply_discount()
    assert testItem.price == 3000