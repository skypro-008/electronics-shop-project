"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Фен", 3000, 20)
item2 = Item("Ноутбук", 25000, 2)
item3 = Item("Маршрутизатор", 3500, 3)

def test_calculate_total_price():
    assert item1.calculate_total_price() == 60000
    assert item2.calculate_total_price() == 50000
    assert item3.calculate_total_price() != 12000


def test_apply_discount():
    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 1500


def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('11') != 10

def test_name():

    assert len(item3.name) > 11


def test__repr__():
    assert repr(item3) == "Item('Маршрутизатор', 3500, 3)"


def test__str__():
    assert str(item2) == 'Ноутбук'
    assert str(item3) == 'Маршрутизатор'