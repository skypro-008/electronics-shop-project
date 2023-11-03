import pytest

from src.item import Item, InstantiateCSVError
import os
"""Здесь надо написать тесты с использованием pytest для модуля item."""

test = Item('смарт часы', 25000, 10)
Item.pay_rate = 0.8


def test_calculate_total_price():
    assert test.calculate_total_price() == 250000


def test_apply_discount():
    Item.pay_rate = 0.8
    assert test.apply_discount() == 20000


def test_name():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон1234'
    assert item.name == 'Смартфон12'
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

def test___repr__():
    item = Item('Телефон', 10000, 5)
    assert repr(item) == "Item(Телефон, 10000, 5)"

def test___str__():
    item = Item('Телефон', 10000, 5)
    assert str(item) == ('Телефон')

def test____add__():
        item1 = Item('Телефон', 10000, 5)
        item2 = Item('Телефон', 10000, 5)
        assert  item1 + item2 == 10




def test_instantiate_from_csv():
    Item.instantiate_from_csv(os.path.join('..', 'src', 'items.csv'))
    assert len(Item.all) == 5
    assert Item.all[0] == {'name': 'Смартфон', 'price': '100', 'quantity': '1'}




def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5


def test_instantiate_from_csv_file_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(os.path.join('..', 'src', 'test_items.csv'))



def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(os.path.join('..', 'sc', 'items.csv'))