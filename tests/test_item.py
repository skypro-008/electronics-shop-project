"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
import os

import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone


@pytest.fixture()
def item():
    item = Item("Смартфон", 10000, 20)
    return item


@pytest.fixture()
def phone():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    return phone


def test_item_initialization(item):
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_string_to_number_1():
    string = "5"
    assert Item.string_to_number(string) == 5


def test_string_to_number_2():
    string = "6.2"
    assert Item.string_to_number(string) == 6


def test_apply_discount(item):
    assert Item.apply_discount(item) == 10000.0


def test_name_setter(item):
    item.name = 'СуперСмартфон'
    assert item._name == "СуперСмарт"


def test__repr__(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test__str__(item):
    assert str(item) == 'Смартфон'


def test__add__1(item, phone):
    assert item + phone == 25
    assert phone + phone == 10
    assert item + 10 == ValueError


def test_instantiate_from_csv():
    with open('../items.csv', encoding='cp1251') as file:
        read = csv.DictReader(file)
        assert read is not None
        for x in read:
            assert "name" in x
            assert "price" in x
            assert "quantity" in x


def test_instantiate_from_csv_file_not():
        with pytest.raises(FileNotFoundError):
                Item.instantiate_from_csv()