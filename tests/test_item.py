"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

@pytest.fixture
def item_test():
    return Item("Миксер", 10.2, 15)

def test_item_init(item_test):

    assert item_test.name == "Миксер"
    assert item_test.price == 10.2
    assert item_test.quantity == 15

def test_item_calculate_total_price (item_test):

    assert item_test.calculate_total_price() == 153

def test_item_apply_discount (item_test):

    Item.pay_rate = 0.5
    item_test.apply_discount()
    assert item_test.price == 5.1
