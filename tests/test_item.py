"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price(item_fixture):
    assert Item.calculate_total_price(item_fixture) == 200000

def test_apply_discount(item_fixture):
    Item.pay_rate = 0.8
    Item.apply_discount(item_fixture)
    assert Item.calculate_total_price(item_fixture) == 160000
