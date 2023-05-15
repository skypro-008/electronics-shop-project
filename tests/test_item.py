"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest
import os


@pytest.fixture
def item():
    return Item("Ноутбук", 50000, 3)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 150000


def test_apply_discount(item):
    Item.pay_rate = 0.8
    assert item.apply_discount() == 40000.0


def test_instantiate_from_csv():
    if os.path.exists('src/items.csv'):
        path = 'src/items.csv'
    else:
        path = '../src/items.csv'
    Item.instantiate_from_csv(path)
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('4') == 4


def test_name(item):
    assert item.name == 'Ноутбук'
    item.name = 'Телефон'
    assert item.name == 'Телефон'
    with pytest.raises(Exception):
        item.name = 'Суперсмартфон'
