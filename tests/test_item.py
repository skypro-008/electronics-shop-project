import pytest
from src.item import Item


item1 = Item("Смартфон", 10000, 20)


def test_init():
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20
    assert Item.all == [item1]
    assert len(Item.all) == 1


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
