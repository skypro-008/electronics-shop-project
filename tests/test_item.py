"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item3 = Item('Пылесос', 45000, 5)


def test_item_init():
    assert item3.name == "Пылесос"
    assert item3.price == 45000
    assert item3.quantity == 5


def test_calculate_total_price():
    assert item3.calculate_total_price() == 225000


def test_apply_discount():
    Item.pay_rate = 0.8
    item3.apply_discount()
    assert item3.price == 36000


