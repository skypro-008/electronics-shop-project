"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def first_item():
    return Item("Лампа", 100, 10)


def test_apply_discount(first_item):
    Item.pay_rate = 0.8
    first_item.apply_discount()
    assert first_item.price == 80


def test_calculate_total_price(first_item):
    assert first_item.calculate_total_price() == 1000


def test_name_setter():
    item = Item("TVset", 50000, 1)
    assert len(item.name) == 5
    item = Item("СуперСмартфон", 500000, 1)
    assert len(item.name) != 10


def test_instantiate_from_csv():
    Item.instantiate_from_csv("./src/items.csv")
    assert len(Item.all) == 5
    Item.all.clear()
    item1 = Item("Product1", 10, 5)
    item2 = Item("Product2", 20, 3)
    assert Item.all == [item1, item2]


def test_string_to_number():
    assert Item.string_to_number('5.0') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    item1 = Item("Товар 1", 100, 5)
    item2 = Item("Товар 2", 200, 3)
    result = item1 + item2
    assert result == 8

