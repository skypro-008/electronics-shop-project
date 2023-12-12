import pytest
import os
from src.item import InstantiateCSVError

from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item1.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 5000


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == 'Смартфон'
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_add():
    item1 = Item('name1', 0, 3)
    item2 = Item("name2", 0, 2)
    assert item1 + item2 == 5
    with pytest.raises(ValueError):
        item1 + 2


def test_instantiate_from_csv():
    with open('test_items.csv', 'w') as file:
        file.write('item1,10.0')
        file.write('item2,20.0')
        file.write('item3')

    try:
        Item.instantiate_from_csv('test_items.csv')
    except InstantiateCSVError as e:
        assert str(e) == "Файл item.csv поврежден"

    try:
        Item.instantiate_from_csv('nonexistent_file.csv')
    except FileNotFoundError as e:
        assert str(e) == "Отсутствует файл item.csv"
    else:
        assert False
