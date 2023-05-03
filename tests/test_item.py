"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item = Item("Product", 10, 5)
    assert item.calculate_total_price() == 50


def test_apply_discount():
    item = Item("Product", 10, 5)
    Item.pay_rate = 0.8  # set the discount to 20%
    item.apply_discount()
    assert item.price == 8

def test_all_instances():
    Item.all.clear()
    item1 = Item("Product1", 10, 5)
    item2 = Item("Product2", 20, 3)
    assert Item.all == [item1, item2]
