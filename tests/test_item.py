"""Тесты для модуля Item"""

import pytest

import cls

import csv

from pytest import fixture

from src.item import Item


@fixture
def Item():
    return Item("Смартфон", 10000, 20)

"""Выводим стоимость товара"""
def test_calculate_total_price(Item):
    assert Item.calculate_total_price == 200000


"""Устанавливаем скидку на товары"""
def test_apply_discount(Item):
    Item.apply_discount()
    assert Item.price == 10000.0


@cls.fixture
def test_instantiate_from_csv(cls) -> None:
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5


def test__repr__():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test__str__():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


    



