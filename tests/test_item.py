import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone
import csv

item1 = Item("Смартфон", 10000, 20)


def test_init():
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20
    assert Item.all == [item1]
    assert len(Item.all) == 1


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_name_getter():
    assert item1.name == "Смартфон"


def test_instantiate_from_csv():
    file = '../src/items.csv'
    Item.instantiate_from_csv(file)
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name_setter():
    item1.name = "Смартфон"
    assert item1.name == "Смартфон"
    item1.name = "АвадаКедавра"
    assert Exception


def test_repr():
    assert repr(item1) == "Item('Смартфон', 8000.0, 20)"


def test_str():
    assert str(item1) == 'Смартфон'


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        file = '../src/item.csv'
        assert Item.instantiate_from_csv(file)


def test_instantiate_csv():
    file = '../src/items2.csv'
    assert Item.instantiate_from_csv(file) == "Файл item.csv поврежден"
