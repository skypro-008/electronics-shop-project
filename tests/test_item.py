"""Тесты для модуля Item"""

import pytest

from pytest import fixture

from item import Item


@fixture
def Item():
    return Item("Смартфон", 10000, 20)

"""Выводим стоимость товара"""
def test_calculate_total_price(Item):
    assert item.calculate_total_price == 200000


"""Устанавливаем скидку на товары"""
def test_apply_discount(Item):
    item.apply_discount()
    assert item.price == 10000.0


def test_instantiate_from_csv(cls) -> None:
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5


    



