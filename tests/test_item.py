"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import os
import pytest
from csv import DictReader


def test_calculate_total_price():
    item = Item("Product", 10, 5)
    assert item.calculate_total_price() == 50


def test_apply_discount():
    item = Item("Product", 10, 5)
    Item.pay_rate = 0.8  # set the discount to 20%
    item.apply_discount()
    assert item.price == 8

def test_all_instances():
    Item.all.clear()
    item1 = Item("Product1", 10, 5)
    item2 = Item("Product2", 20, 3)
    assert Item.all == [item1, item2]


@pytest.fixture(scope="module")
def csv_data():
    filedir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(f'{filedir}/../src', 'items.csv'), 'r+', encoding='windows-1251') as csv_file:
        csv_reader = DictReader(csv_file)
        return [item for item in csv_reader]

def test_load_csv(csv_data):
    assert len(csv_data) > 0

def test_instantiate_from_csv(csv_data):
    Item.instantiate_from_csv()
    assert len(Item.all) == len(csv_data)

def test_string_to_number():
    assert Item.string_to_number('15') == 15
    assert Item.string_to_number('15.5') == 15
    assert Item.string_to_number('17.0') == 17


