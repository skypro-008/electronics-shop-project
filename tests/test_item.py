"""Здесь надо написать тесты с использованием pytest для модуля item."""

from item import Item


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000

    item2 = Item("Ноутбук", 20000, 5)
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item1.apply_discount()
    assert item1.price == 8000.0

    item2 = Item("Ноутбук", 20000, 5)
    item2.apply_discount()
    assert item2.price == 20000


def test_apply_discount_with_zero_discount():
    item1 = Item("Смартфон", 10000, 20)
    item1.apply_discount(0)
    assert item1.price == 10000

    item2 = Item("Ноутбук", 20000, 5)
    item2.apply_discount(0)
    assert item2.price == 20000


def test_apply_discount_with_hundred_percent_discount():
    item1 = Item("Смартфон", 10000, 20)
    item1.apply_discount(100)
    assert item1.price == 0.0

    item2 = Item("Ноутбук", 20000, 5)
    item2.apply_discount(100)
    assert item2.price == 0.0

def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'