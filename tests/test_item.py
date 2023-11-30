import os

import pytest
from src.item import Item


@pytest.fixture()
def total_1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(total_1):
    assert total_1.calculate_total_price() == 200000


def test_apply_discount(total_1):
    total_1.pay_rate = 0.8
    total_1.apply_discount()
    assert total_1.price == 8000.0


@pytest.fixture()
def total_2():
    return Item("Ноутбук", 20000, 5)


def test_calculate_total_2_price(total_2):
    assert total_2.calculate_total_price() == 100000


def test_apply_discount_2(total_2):
    total_2.pay_rate = 0.8
    total_2.apply_discount()
    assert total_2.price == 16000.0


def test_name_setter():
    item = Item('Компьютер', 100, 2)
    assert item.name == 'Компьютер'


def test_instantiate_from_csv():
    Item.instantiate_from_csv(r"C:/Users/Admin/PycharmProjects/electronics-shop-project/src/items.csv")
    assert len(Item.all) == 5


def test_repr_and_str():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
