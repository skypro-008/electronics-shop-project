import pytest
from src.item import Item

def test_item_name_property():
    item = Item("1", "Test Item", 10)
    assert item.name == "Test Item"
    item.name = "This is a very long name for an item"
    assert item.name == "This is a "

def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert len(items) == 3
    assert items[0].name == "Item1"
    assert items[1].name == "Item2"
    assert items[2].name == "Item3"

def test_string_to_number():
    number = Item.string_to_number("100")
    assert number == 100