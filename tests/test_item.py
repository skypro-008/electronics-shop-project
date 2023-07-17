import pytest
from src import item


def test_constructor():
    test_item = item.Item("Телевизор", 40000, 5)
    assert test_item.name == "Телевизор"
    assert test_item.price == 40000
    assert test_item.quantity == 5

