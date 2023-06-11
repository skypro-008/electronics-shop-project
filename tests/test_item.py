"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
import os

import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone


def test_constructor():
    item = Item("Товар 1", 1000.5, 10)
    assert item.name == "Товар 1", "Неверный формат данных: должен быть текст"
    assert item.price == 1000.5, "Неверный формат данных: должено быть число с плавающей точкой"
    assert item.quantity == 10, "Неверный формат данных: должен быть число"
    assert item.name == 'Товар 1'


def test_calculate_total_price():
    item = Item("Товар 2", 2000, 15)
    assert item.calculate_total_price() == 30000, "Неверно произведен расчет"


def test_apply_discount():
    item = Item("Товар 3", 500.75, 25)
    assert item.price == 500.75, "Неверно передаются данные"
    item.pay_rate = 0.75
    item.apply_discount()
    assert item.price == 375.5625, "Неверно произведен расчет"


def test_all():
    Item.all.clear()
    assert Item.all == []
    item1 = Item("Товар 1", 1000, 5)
    assert Item.all == [item1], "Неверный формат ячейки"
    item2 = Item("Товар 2", 2000, 10)
    assert Item.all == [item1, item2], "Неверный формат ячеек"
    item3 = Item("Товар 3", 3000, 15)
    assert Item.all == [item1, item2, item3], "Неверный формат ячеек"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_repr():
    item1 = Item('Smartphone', 10000, 20)
    assert repr(item1) == "Item('Smartphone', 10000, 20)"


def test_str():
    item1 = Item('Smartphone', 10000, 20)
    assert str(item1) == 'Smartphone'


def test_addition():
    item1 = Item('Telephone', 10000, 39)
    phone1 = Phone("iPhone 15", 140000, 6, 2)
    assert item1 + phone1 == 45
    assert phone1 + phone1 == 12
    with pytest.raises(ValueError):
        assert item1 + 10 == 49
        assert phone1 + 5 == 11


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    assert len(Item.all) == 5
    with pytest.raises(FileNotFoundError):
        Item.instantiate_csv('../tests/items.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_csv('../tests/items1.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_csv('../tests/items2.csv')