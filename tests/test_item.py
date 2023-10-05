"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
item_1 = Item("TV", 20000, 100)
Item.pay_rate = 2.0

def test_calculate_total_price():
    assert Item("TV", 20000, 100).calculate_total_price == 2000000
    assert Item("TV", 0, 100).calculate_total_price == 0


def test_apply_discount():
    item_1.apply_discount()
    assert 50000 * Item.pay_rate == float(100000)
