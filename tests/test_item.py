"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def item():
    return Item("Ноутбук", 50000, 3)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 150000


def test_apply_discount(item):
    Item.pay_rate = 0.8
    assert item.apply_discount() == 40000.0
