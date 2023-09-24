"""Здесь надо написать тесты с использованием pytest для модуля item."""
import os.path

import pytest

from src.item import Item
import csv

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

def test_item():
    assert item1.price * item1.pay_rate == 10000.0
    assert item2.name == "Ноутбук"
    assert Item.string_to_number('7') == 7
    assert type(Item.string_to_number('7')) == int
    assert type(Item.all) == list
    assert os.path.isfile('../src/items.csv') == True
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
    # assert Item.instantiate_from_csv("file.txt") == "Отсутствует файл"
    assert Item.instantiate_from_csv() is None #==

def test_instantiate_from_csv():
    with open('items.csv') as file:
        read = csv.DictReader(file)
        assert read is not None
        for x in read:
            assert "name" in x
            assert "price" in x
            assert "quantity" in x

def test_instantiate_from_csv_file_not():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('juguig.csv')
