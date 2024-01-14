import csv
import os.path

import pytest

from src.item import Item
from src.MyExceptions import InstantiateCSVError


def test_instantiate_from_csv():
    Item.instantiate_from_csv("src/items.csv")
    assert len(Item.all) == 5

    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "src", "items.csv")) as file:
        items = csv.DictReader(file)
        for i, item in enumerate(items):
            assert Item.all[i].name == item["name"]
            assert Item.all[i].price == item["price"]
            assert Item.all[i].quantity == item["quantity"]


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_instantiate_from_csv_err():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('item.csv')

    with pytest.raises(InstantiateCSVError, match=''):
        Item.instantiate_from_csv('src/items_test.csv')
    