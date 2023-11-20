import pytest

from src.item import Item

item_1 = Item("Смартфон", 10000, 5)
item_2 = Item("Ноутбук", 25000, 3)
item_1.pay_rate = 0.8
item_2.pay_rate = 0.95


def test_valid_item():
    assert item_1.name == "Смартфон"
    assert item_1.price == 10000
    assert item_1.quantity == 5

    assert item_2.name == "Ноутбук"
    assert item_2.price == 25000
    assert item_2.quantity == 3


def test_calculate_total_price():
    assert item_1.calculate_total_price() == 50000
    assert item_2.calculate_total_price() == 75000


def test_apply_discount():
    item_1.apply_discount()
    assert item_1.price == 8000
    item_2.apply_discount()
    assert item_2.price == 23750
