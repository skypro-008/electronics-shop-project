"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def test_item():
    return Item("Watches", 10000, 5)

def test_calculate_total_price():
    assert test_item.calulate_total_price() == 50000

def test_apply_discount():
    assert test_item.apply_discount() == 8000
