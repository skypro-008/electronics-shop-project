"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import csv
import os

from src.item import Item, InstantiateCSVError
from src.phone import Phone

item1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000.0


def test_class_Item():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.5") == 5
    assert Item.string_to_number("5.0") == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_instantiate_from_csv_1():
    with pytest.raises(FileNotFoundError):
        Item.csv_file = os.path.join(os.path.dirname(__file__), "tems.csv")
        with open(Item.csv_file, newline="", encoding="latin-1") as file:
            read_file = csv.DictReader(file)


def test_name():
    assert item1.name == "Смартфон"


def test_name():
    item1.name = "Ноутбук"
    assert item1.name == "Ноутбук"


def test__str__():
    items1 = Item("Смартфон", 10000, 20)
    assert str(items1) == "Смартфон"
    items1 = Item("Ноутбук", 20000, 20)
    assert str(items1) == "Ноутбук"


def test__repr__():
    items1 = Item("Смартфон", 10000, 20)
    assert repr(items1) == "Item('Смартфон', 10000, 20)"
    items1 = Item("Ноутбук", 20000, 20)
    assert repr(items1) == "Item('Ноутбук', 20000, 20)"


class Examination:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


def test__add__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    cls1 = Examination("Смартфон", 10000, 20)
    assert phone1 + cls1 is None
    assert item1 + cls1 is None
