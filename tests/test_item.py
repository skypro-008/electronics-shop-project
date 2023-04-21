import pytest

from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest


@pytest.fixture
def item():
    return Item("item1", 10, 5)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50.0


def test_apply_discount(item):
    Item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 9.0


def test_item_initialization(item):
    assert item.name == "item1"
    assert item.price == 10
    assert item.quantity == 5
    assert len(Item.all) == 3
    assert Item.all[0] == item
