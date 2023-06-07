from src.item import Item, InstantiateCSVError
from src.phone import Phone
import csv
import pytest
import os


def test_item():
    item = Item('test', 10000, 10)

    # TestCase #1 name
    assert item.name == "test"

    # TestCase #2 price
    assert item.price == 10000

    # TestCase #3 quantity
    assert item.quantity == 10

    # TestCase #4 calculate_total_price
    assert item.calculate_total_price() == 100000

    # TestCase #5 apply_discount
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000

def test_from_csv():
    PATH_TO_ITEMS = '/home/rusanov/Skypro_study/Course4/electronics-shop-project/src/items.csv'
    all = []
    with open(PATH_TO_ITEMS, encoding='Windows-1251') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Item(row['name'], int(row['price']), int(row['quantity']))
            all.append(Item(row['name'], int(row['price']), int(row['quantity'])))

    assert len(all) == 5
    item_3 = all[3]
    assert item_3.name == 'Мышка'
    assert item_3.price == 50
    assert item_3.quantity == 5


def test_name():
    item = Item('test', 10000, 10)
    assert item.name == 'test'

    with pytest.raises(ValueError):
        item.name = 'Больше 10 символов'


def test_string_to_number():
    assert Item.string_to_number('1000') == 1000
    assert Item.string_to_number('1000.0') == 1000
    assert Item.string_to_number('5.99') == 5

    with pytest.raises(ValueError):
        Item.string_to_number('word')


def test_repr_str():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'

def test_add():
    item1 = Item("Смартфон", 10000, 50)
    phone1 = Phone("iPhone 14", 120_000, 30, 2)
    assert item1 + phone1 == 80

    with pytest.raises(TypeError):
        item1 + 100
        phone1 + '200'


def test_instantiate_from_csv_missing_file():

    with pytest.raises(FileNotFoundError):
       Item.instantiate_from_csv('file_not_exist.csv')


def test_instantiate_from_csv_invalid_file():

    with pytest.raises(InstantiateCSVError):
       raise InstantiateCSVError























