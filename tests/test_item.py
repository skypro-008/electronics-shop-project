"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item('Наушники', 5000, 10)


def test_item_init(item1):
    assert item1.name == 'Наушники'
    assert item1.price == 5000
    assert item1.quantity == 10


def test_item_calculate_total_price(item1):
    assert item1.calculate_total_price() == 50000


def test_item_apply_discount(item1):
    pay_rate = 0.5
    assert item1.price * pay_rate == 2500


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    item1 = Item.all[4]
    assert item1.name == 'Клавиатура'
    assert item1.price == 75
    assert item1.quantity == 5


def test_string_to_number():
    assert Item.string_to_number('4') == 4


def test_item_repr(item1):
    assert repr(item1) == "Item('Наушники', 5000, 10)"


def test_item_str(item1):
    assert str(item1) == 'Наушники'

def test_item_add(item1):
    item2 = Item('Клавиатура', 10000, 5)
    assert item1 + item2 == 15
