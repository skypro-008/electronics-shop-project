"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000

def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item1.apply_discount()
    assert item1.price == Item.pay_rate * 10000

def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test__repr__():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test__str__():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'



