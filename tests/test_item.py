"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

import pytest
@pytest.fixture()
def item2():
    return Item("Ноутбук", 20000, 5)

def test_calculate_total_price(item2):
    assert item2.calculate_total_price() == 20000 * 5

def test_apply_discount(item2):
    item2.pay_rate = 0.4
    item2.apply_discount()
    assert item2.price == 0.4 * 20000