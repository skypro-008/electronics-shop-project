"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def item_test():
    return Item("Ноутбук", 50000, 5)

def test_item_init(item_test):
    assert item_test.name == "Ноутбук"
    assert item_test.price == 50000
    assert item_test.quantity == 5

def test_calculate_total_price(item_test):
    assert item_test.calculate_total_price() == 250000

def test_apply_discount(item_test):
    Item.pay_rate = 0.5
    item_test.apply_discount()
    assert item_test.price == 25000