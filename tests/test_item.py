"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

@pytest.fixture
def item_data():
    item = Item("Смартфон", 10000, 20)
    return item
def test_item_calculate_total_price(item_data):
    assert item_data.calculate_total_price() == 200000

def test_item_apply_discount(item_data):
    item_data.pay_rate = 0.8
    assert item_data.apply_discount() == 8000