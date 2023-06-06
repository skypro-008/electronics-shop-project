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


def test_name(items):
    items.name = "Ноутбук"
    assert items.name == "Ноутбук"
    items.new_name = "Смартфон"
    assert items.new_name == "Смартфон"
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr():
    item = Item("Ноутбук", 32000, 15)
    assert repr(item) == "Item('Ноутбук', 32000, 15)"


def test_str():
    item = Item("Ноутбук", 32000, 15)
    assert str(item) == 'Ноутбук'


