"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
# from src.phone import Phone
import pytest
import os


@pytest.fixture
def item_1():
    return Item("Ноутбук", 50000, 3)


@pytest.fixture
def item_2():
    return Item("Телевизор", 65000, 2)


# @pytest.fixture
# def phone_1():
#     return Phone("Samsung", 34000, 8, 0)


# @pytest.fixture
# def phone_2():
#     return Phone("Sony", 46000, 6, 2)


def test__repr__(item_1):
    assert repr(item_1) == "Item('Ноутбук', 50000, 3)"


def test__str__(item_1):
    assert str(item_1) == 'Ноутбук'


def test__add__(item_1, item_2):
    assert item_1 + item_2 == 5
    with pytest.raises(Exception):
        item_1 + 3
        '10' + item_2

# Вариант для сложения строго в определенном классе
# def test__add__(item_1, item_2, phone_1, phone_2):
#     assert item_1 + item_2 == 5
#     with pytest.raises(Exception):
#         item_1 + phone_2
#         phone_1 + item_2


def test_calculate_total_price(item_1):
    assert item_1.calculate_total_price() == 150000


def test_apply_discount(item_1):
    Item.pay_rate = 0.8
    assert item_1.apply_discount() == 40000.0


def test_instantiate_from_csv():
    if os.path.exists('src/items.csv'):
        path = 'src/items.csv'
    else:
        path = '../src/items.csv'
    Item.instantiate_from_csv(path)
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('4') == 4


def test_name(item_1):
    assert item_1.name == 'Ноутбук'
    item_1.name = 'Телефон'
    assert item_1.name == 'Телефон'
    with pytest.raises(Exception):
        item_1.name = 'Суперсмартфон'
