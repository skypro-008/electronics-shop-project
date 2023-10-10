"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_item():
    return Item("TV", 10000, 5)


def test_calculate_total_price():
    item = Item("TV", 10000, 2)
    assert item.calculate_total_price() == 20000


def test_apply_discount():
    item = Item("TV", 10000, 2)
    item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 5000
