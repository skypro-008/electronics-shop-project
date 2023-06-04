"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_item():
    return Item("test_notebook", 35000, 4)


def test_init(test_item):
    assert test_item.name == "test_notebook"
    assert test_item.price == 35000
    assert test_item.quantity == 4


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 140000


def test_apply_discount(test_item):
    test_item.pay_rate = 0.9
    test_item.apply_discount()
    assert test_item.price == 31500
