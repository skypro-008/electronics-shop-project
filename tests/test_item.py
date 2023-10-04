"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item('bla', 10000, 10)
item2 = Item('qla', 10000, 10)


def test_calculate_total_price():
    assert item1.price + item2.price == 20000


def test_apply_discount():
    assert Item.pay_rate * item1.price == 10000


def test__init__():
    assert item1.name == 'bla'
    assert item2.price == 10000
    assert item1.quantity == 10
    assert Item.all == [item1, item2]
