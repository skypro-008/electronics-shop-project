"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Смартфон", 10000, 0)


def test__repr__():
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test__str__():
    assert str(item1) == "Смартфон"


def test_alculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 0


def test_apply_discount():
    assert item1.apply_discount(0.2) == 2000
    assert item1.apply_discount(0) == 0


def test_name():
    assert item1.name == 'Смартфон'
    item1.name = 'Телефон'
    assert item1.name == 'Телефон'


def test_string_to_number():
    assert Item.string_to_number('1') == 1
    assert Item.string_to_number('1.0') == 1
    assert Item.string_to_number('1.1') == 1
