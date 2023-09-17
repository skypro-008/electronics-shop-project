"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


def test_calculate_total_price():
    item = Item("Телефон", 10000, 5)
    assert item.calculate_total_price() == 50000

def test_apply_discount():
    item = Item("Телефон", 10000, 5)
    assert item.apply_discount() == 10000

def test_name():
    item = Item("Телефон", 10000, 5)
    item.name = 'Калькулятор'
    assert item.name == 'Калькулято'

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr():
    item = Item("Телефон", 10000, 5)
    assert repr(item) == "Item('Телефон', 10000, 5)"

