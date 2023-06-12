"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_init():
    item1 = Item("Смартфон", 10000, 20)

    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20

    item2 = Item("Ноутбук", 20000, 5)

    assert item2.name == "Ноутбук"
    assert item2.price == 20000
    assert item2.quantity == 5


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.apply_discount() == 10000
    assert item2.apply_discount() == 20000


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_name():
    item = Item('Смартфон', 10000, 5)
    assert item.name == 'Смартфон'

    # item = Item('СуперСмартфон', 10000, 5)
    # assert item.name == 'Длина наименования товара превышает 10 символов.'


# def test_instantiate_from_csv():
#     item = Item()
#     assert len(item.all) == 5

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    # assert Item.string_to_number('5.0') == 5
    # assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item('Смартфон', 10000, 20)
    assert repr(item1) == 'Item(Смартфон, 10000, 20)'


def test_str():
    item1 = Item('Смартфон', 10000, 20)
    assert str(item1) == 'Смартфон'
