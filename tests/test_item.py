import os

import pytest

from src.item import Item, InstantiateCSVError


@pytest.fixture
def test_bad_filename():
    Item.csv_file_name = 'items_b.csv'
    Item.instantiate_from_csv('items_b.csv')


@pytest.fixture
def test_init(test_item):
    assert test_item.name == "Ноутбук"
    assert test_item.price == 20000
    assert test_item.quantity == 5


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 100000


def test_apply_discount(test_item):
    test_item.apply_discount()
    assert test_item.price == 20000
    test_item.pay_rate = 0.8
    test_item.apply_discount()
    assert test_item.price == 16000.0


def test_name_setter(test_item):
    test_item.name = "Notebook"
    assert test_item.name == "Notebook"


def test_name_getter(test_item):
    assert test_item.name == "Ноутбук"


def test_instantiate_from_csv():
    Item.all.clear()
    Item.instantiate_from_csv()
    assert Item.all[0].name == "Смартфон"
    assert Item.all[1].price == "1000"
    assert Item.all[4].quantity == "5"
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(test_item):
    assert repr(test_item) == "Item('Ноутбук', 20000, 5)"


def test_str(test_item):
    assert str(test_item) == 'Ноутбук'

def test_instantiate_from_csv_error():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('does_not_exists.csv')

def test_instantiate_from_csv_error():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('corrupted.csv')



    # def test_add(test_item):
    #     phone1 = Phone("iPhone 14", 120_000, 5, 2)
    #     assert test_item + test_item == 10
    #     assert phone1 + phone1 == 10
    #     assert test_item + phone1 == 10
    #     assert phone1 + test_item == 10

""" pytest --cov=src --cov-report=html """