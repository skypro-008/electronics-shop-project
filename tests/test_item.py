"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def test_item():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    return [item1, item2]


def test_calculate_total_price(test_item):
    assert test_item[0].calculate_total_price() == 200000
    assert test_item[1].calculate_total_price() == 100000


def test_apply_discount(test_item):
    Item.pay_rate = 0.8
    test_item[0].apply_discount()
    assert test_item[0].price == 8000.0
    assert test_item[1].price == 20000
