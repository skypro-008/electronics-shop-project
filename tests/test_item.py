"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def my_item():
    return Item("bananas", 10, 2)


def test_item_init(my_item):
    assert my_item.name == "bananas"
    assert my_item.price == 10
    assert my_item.quantity == 2

def test_calculate_total_price(my_item):
    assert my_item.calculate_total_price() == 20

def test_apply_discount():
    item = Item("apples", 5, 2)
    item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 4.5

def test_instantiate_from_csv(my_item):
    assert len(Item.all) == 4

def test_string_to_number(my_item):
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


