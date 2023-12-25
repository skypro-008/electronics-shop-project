import csv
import os.path

from src.item import Item
from src.phone import Phone


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


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
