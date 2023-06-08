"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item('Наушники', 5000, 10)


def test_item_init(item1):
    assert item1.name == 'Наушники'
    assert item1.price == 5000
    assert item1.quantity == 10


def test_item_calculate_total_price(item1):
    assert item1.calculate_total_price() == 50000


def est_item_apply_discount(item1):
    Item.pay_rate = 0.5
    assert item1.apply_discount() == 2500.0
