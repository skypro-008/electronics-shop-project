"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

test_item = Item("Watches", 10000, 5)
def test_calculate_total_price():
    assert test_item.calculate_total_price() == 50000

def test_apply_discount():
    assert test_item.apply_discount() == 8000

def test_str():
    assert test_item.__str__() == "товар Watches, цена за единицу 10000, количество 5"

def test_repr():
    assert test_item.__repr__() == "Item('Watches', 10000, 5)"

