"""Тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount():
    item = Item("Смартфон", 10000, 20)

    Item.pay_rate = 0.8
    item.apply_discount(0.2)

    assert item.price == 1600.0000000000002

def test_apply_discount_for_all_items():

    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)


    Item.pay_rate = 0.8

    item1.apply_discount(1)
    item2.apply_discount(1)


    assert item1.price == 8000
    assert item2.price == 16000
    assert item1.calculate_total_price() == 128000.0
    assert item2.calculate_total_price() == 64000.0