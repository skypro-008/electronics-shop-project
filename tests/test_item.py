"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

import pytest

from src.error import InstantiateCSVError
from src.item import Item
from src.phone import Phone

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Смартфон", 10000, 0)
phone1 = Phone("iPhone 14", 120_000, 5, 2)
phone2 = Phone("iPhone 14", 120_000, 5, 0)


def test__repr__():
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test__str__():
    assert str(item1) == "Смартфон"


def test_alculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 0


def test_apply_discount():
    assert item1.apply_discount(0.2) == 2000
    assert item1.apply_discount(0) == 0


def test_name():
    assert item1.name == 'Смартфон'
    item1.name = 'Телефон'
    assert item1.name == 'Телефон'


def test_string_to_number():
    assert Item.string_to_number('1') == 1
    assert Item.string_to_number('1.0') == 1
    assert Item.string_to_number('1.1') == 1


def test__add__():
    assert item1 + item2 == 20
    assert item1 + phone1 == 25
    assert phone1 + item1 == 25


def test_number_of_sim():
    with pytest.raises(ValueError):
        e = Phone("Phone", 1000.0, 10, 0)
        e.number_of_sim(0)


def test_instantiate_from_csv_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('../src/NotFound.csv')


def test_instantiate_from_csv():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('./tests/items_error.csv')
