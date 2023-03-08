"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

import pytest


@pytest.fixture
def item():
    return Item('test', 8000, 2)

def test_item_init(item):
    """
    Тест класса
    """
    assert type(item.name) == str
    assert type(item.price) == int
    assert type(item.quantity) == int

def test_item_init_2(item):
    """
    Тест значений класса
    """
    assert item.name == 'test'
    assert item.price == 8000
    assert item.quantity == 2

def test_calculate_total_price(item):
    """
    Тест общей стоимости конкретного товара в магазине
    """
    assert item.calculate_total_price() == 16000

def test_apply_discount(item):
    """
    Тест применения установленной скидки для конкретного товара
    """
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 4000