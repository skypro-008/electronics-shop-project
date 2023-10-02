"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_instance_item():
    item = Item(name='Device', price=99.9, quantity=10)
    assert item.name == 'Device'
    assert item.price == 99.9
    assert item.quantity == 10


def test_calculate_price():
    item = Item(name='Device', price=99.9, quantity=10)
    assert item.calculate_total_price() == 999.0


def test_class_param():
    item = Item(name='Device', price=99.9, quantity=10)
    assert item.pay_rate == 1.0
    assert Item.pay_rate == 1.0
    Item.pay_rate = 1.5
    assert item.pay_rate == 1.5
    assert Item.pay_rate == 1.5


def test_apply_discount():
    item = Item(name='Device', price=99.9, quantity=10)
    assert item.price == 99.9
    Item.pay_rate = 1.5
    assert item.apply_discount() is None
    assert item.price == 149.85
