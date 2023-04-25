"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_class_item():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000
    assert item1.apply_discount() == 8000


def test_name():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.2") == 5
    assert Item.string_to_number("100.5") == 100


def test_name():
    item = Item('Телефон', 10000, 5)
    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
