"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    epm_1 = Item('Suren', 14, 20)
    assert epm_1.calculate_total_price() == 280


def test_apply_discount():
    epm_1 = Item('Suren', 14, 20)
    Item.pay_rate = 0.5
    epm_1.apply_discount()
    assert epm_1.price == 7


def test_main():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000
    assert item2.price == 20000
    for object_ in Item.all:
        assert isinstance(object_, Item)
