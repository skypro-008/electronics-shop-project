"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def items():
    return Item('str', 200000, 20)

def test_item(items):
    assert items.name == 'str'
    assert items.price == 200000
    assert items.quantity == 20
    assert items.calculate_total_price() == 200000 * 20

