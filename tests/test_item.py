"""Здесь тесты с использованием pytest для модуля item."""

from src.item import Item


def test_init():
    item = Item('test', 200.0, 100)
    Item.pay_rate = 0.5
    assert item.name == 'test'
    assert item.price == 200.0
    assert item.quantity == 100
    item.apply_discount()
    assert item.calculate_total_price() == 10000.0
