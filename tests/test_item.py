"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone
item1 = Item("Фен", 3000, 20)
item2 = Item("Ноутбук", 25000, 2)
item3 = Item("Маршрутизатор", 3500, 3)
phone1 = Phone("iPhone 14", 120_000, 5, 2)
phone2 = Phone("iPhone X", 80_000, 10, 1)

def test_calculate_total_price():
    assert item1.calculate_total_price() == 60000
    assert item2.calculate_total_price() == 50000
    assert item3.calculate_total_price() != 12000


def test_apply_discount():
    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 1500

def test_add_():
    assert phone1 + item2 != 7
    assert phone2 + phone1 == 15
    assert item1 + item3 == 23
def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('11') != 10

def test_number_of_sim():
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0

def test_name():
    with pytest.raises(Exception):
        item3.name = 13
    assert len(item2.name) == 7


def test__repr__():
    assert repr(item3) == "Item('Маршрутизатор', 3500, 3)"
    assert repr(phone2) == "Phone('iPhone X', 80000, 10, 1)"

def test__str__():
    assert str(item2) == 'Ноутбук'
    assert str(item3) == 'Маршрутизатор'
    assert str(phone1) == 'iPhone 14'