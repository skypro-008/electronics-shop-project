import pytest
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
Item.pay_rate = 0.8
def test_calculate_total_price():
    assert Item.calculate_total_price(item1) == 200000
    assert Item.calculate_total_price(item2) == 100000

def test_apply_discount():
    assert Item.apply_discount(item1) == 8000.0