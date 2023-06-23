"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src import item
from src.item import Item, InstantiateCSVError


def test_calculate_total_price():
    assert item.Item("Смартфон", 10000, 20).calculate_total_price() == 200000
    assert item.Item("Ноутбук", 20000, 5).calculate_total_price() == 100000


def test_apply_discount():
    test_item = item.Item("Смартфон", 10000, 20)
    item.Item.pay_rate = 0.3
    test_item.apply_discount()
    assert test_item.price == 3000


def test_name():
    item1 = Item("Смартфон", 10000, 20)
    item1.name = "НеСмартфон"
    assert item1.name == 'НеСмартфон'

    item1.name = "СуперПуперМегаДрайвДваНеСмартфон"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_item_magic_mathods():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон',10000,20)"
    assert str(item1) == 'Смартфон'


def test_item_add():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Смартфон2", 10000, 22)
    assert item1 + item2 == 42
    assert item1 + "stroka" == None

def test_item_file():
    FILE_PATH = './src/'
    FILE_NAME1 = 'items1.csv'
    FILE_NAME2 = 'items2.csv'
    with pytest.raises(FileNotFoundError) as e:
        open(FILE_PATH + FILE_NAME1, 'r', newline='')

    with pytest.raises(KeyError) as e:
        open(FILE_PATH + FILE_NAME2, 'r', newline='')

