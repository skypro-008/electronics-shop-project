"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

@pytest.fixture()
def item_example():
    return Item("Наушники", 5000, 10)

def test_item_calculate_total_price(item_example):
    assert item_example.calculate_total_price() == 50000

def test_item_apply_discount(item_example):
    assert item_example.apply_discount() == 5000







