"""Тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount():
    item = Item("Смартфон", 10000, 20)

    Item.pay_rate = 0.8
    item.apply_discount(0.8)

    assert item.price == 8000

def test_apply_discount_for_all_items():

    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)


    Item.pay_rate = 0.8

    item1.apply_discount(0.8)
    item2.apply_discount(0.5)


    assert item1.price == 8000
    assert item2.price == 10000
    assert item1.calculate_total_price() == 128000.0
    assert item2.calculate_total_price() == 40000.0

from src.item import Item


def test_item():

    # создание и проверка первого объекта
    item1 = Item('Телефон', 10000, 5)
    assert len(Item.all) == 1
    assert item1.name == 'Телефон'
    assert item1.price == 10000
    assert item1.quantity == 5
    assert item1.calculate_total_price() == 50000.0

    # изменение свойства name
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'

    # создание и проверка второго объекта с длинным name
    big_item = Item('СуперСмартфон', 5000, 10)
    assert big_item.name == 'СуперСмартфон'

    # создание объектов из файла csv
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 7
    item2 = Item.all[0]
    assert item2.name == 'Смартфон'
    assert item2.price == 10000
    assert item2.quantity == 5
    assert item2.calculate_total_price() == 50000.0

    # проверка метода string_to_number
    assert Item.string_to_number('5') == 5.0
    assert Item.string_to_number('5.0') == 5.0
    assert Item.string_to_number('5.5') == 5.5

def test___repr__():
    item = Item("Ноутбук", 20000, 5)
    assert item.__repr__() == "Item('Ноутбук', 20000, 5)"
def test___str__():
    item = Item("Ноутбук", 20000, 5)
    assert item.__str__() == 'Ноутбук'