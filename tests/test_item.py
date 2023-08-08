"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount():
    assert Item.pay_rate == 1

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item_test = Item.all[3]
    assert item_test.name == "Мышка"
    for product in Item.all:
        assert isinstance(product, Item)

    with pytest.raises(FileNotFoundError) as e:
        Item.instantiate_from_csv()
        assert str(e) == "Файл item.csv отсутствует"

    with pytest.raises(InstantiateCSVError) as e:
        Item.instantiate_from_csv()
        assert str(e) == "Файл item.csv поврежден"

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test__repr__():
    assert Item.__repr__(Item('Смартфон', 10000, 20)) == "Item('Смартфон', 10000, 20)"

def test__str__():
    assert str('Смартфон') == 'Смартфон'

def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2


def test__add__():
    phone1 = Phone('iPhone 14', 120000, 5, 2)
    item1 = Item('Смартфон', 10000, 20)
    assert phone1 + item1 == 25
    assert phone1 + phone1 == 10