from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""

test = Item('смарт часы', 25000, 10)
Item.pay_rate = 0.8


def test_calculate_total_price():
    assert test.calculate_total_price() == 250000


def test_apply_discount():
    Item.pay_rate = 0.8
    assert test.apply_discount() == 20000
