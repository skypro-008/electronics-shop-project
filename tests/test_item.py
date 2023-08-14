"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def test_item():
    return Item(name="Phone", price=1000, quantity=10)


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 10000


def test_apply_discount(test_item):
    test_item.pay_rate = 0.8
    test_item.apply_discount()
    assert 1000 * test_item.pay_rate == test_item.price
