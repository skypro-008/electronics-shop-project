"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item

def test_init(some_item):
    assert some_item.name == "Смартфон"
    assert some_item.price == 10000
    assert some_item.quantity == 5

def test_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 50000


def test_apply_discount(some_item):
    some_item.pay_rate = 0.5
    some_item.apply_discount()
    assert some_item.price == 5000

def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_name(some_item):
    some_item.name = 'Смартфон'
    assert some_item.name == 'Смартфон'
    some_item.name = 'СуперСмартфон'
    assert some_item.name == 'СуперСмарт'