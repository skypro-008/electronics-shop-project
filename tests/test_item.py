"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    prod1 = Item("Телевизор", 50, 5)

    assert Item.calculate_total_price(prod1) == 250

def test_apply_discount():
    prod1 = Item("Телевизор", 50, 5)
    pay_rate = 2

    assert Item.apply_discount(prod1) == None




