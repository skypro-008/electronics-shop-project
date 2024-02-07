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

def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    item_two = Item.all[1]
    assert item_two.name == 'Ноутбук'

def test_string_to_number():
    assert Item.string_to_number('4') == 4
    assert Item.string_to_number('4.0') == 4
    assert Item.string_to_number('4.7') == 4

def test_repr(item_example):
    assert repr(item_example) == "Item('Наушники', 5000, 10)"

def test_str(item_example):
    assert str(item_example) == "Наушники"



