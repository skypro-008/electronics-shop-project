"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item
from src.phone import Phone

from src.item import Item

def test_calculate_total_price():
    item1 = Item("Смартфон", 50000, 30)
    item2 = Item("Ноутбук", 80000, 20)

    assert item1.calculate_total_price() == 1500000
    assert item2.calculate_total_price() == 1600000

def test_apply_discount():
    item1 = Item("Смартфон", 50000, 30)
    item2 = Item("Ноутбук", 80000, 20)


    assert item1.price == 50000
    assert item2.price == 80000

    Item.pay_rate = 0.8

    item1.apply_discount()

    assert item1.price == 40000
    assert item2.price == 80000

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5.5

def test_name():
    item = Item
    item.name = "Apple"
    assert item.name == "Apple"

def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == "Смартфон"

def test_raise():
    item1 = Item("Смартфон", 10000, 20)
    with pytest.raises(Exception):
        item1.name = 'Смартфон Айфон'