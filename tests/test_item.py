"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

from src.item import Item, InstantiateCSVError
import pytest


@pytest.fixture
def item():
    item = Item("Смартфон", 10000, 20)
    return item


def test_calculated_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    assert item.price == 10000


def test_name(item):
    item.name = "СуперСмартфон"
    assert item.name == "СуперСмарт"


def test_instantiate_from_csv(item):
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5


def test_string_to_number(item):
    assert Item.string_to_number('6.5') == 6


def test___repr__(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test___str__(item):
    assert str(item) == 'Смартфон'


def test_instantiate_from_csv_not_file():
    with pytest.raises(FileNotFoundError):
        with open('src/items_1.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)


def test_instantiate_from_csv_broken_file():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
