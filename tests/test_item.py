from src.item import Item


import pytest



def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert Item.calculate_total_price(item1) == 200000

def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    Item.apply_discount(item1)
    assert item1.price == 8000