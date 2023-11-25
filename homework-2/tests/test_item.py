
import pytest
from src.item import Item

def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert len(items) == 3

def test_string_to_number():
    result = Item.string_to_number("100")
    assert result == 100