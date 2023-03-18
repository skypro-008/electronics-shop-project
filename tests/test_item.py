"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import *

def test_calculate_total_price():
    item3 = Item("cat", 3000, 10)
    total_price = item3.calculate_total_price()
    assert total_price == 30000

def test_apply_discount():
    item3 = Item("cat", 3000, 10)
    item3.pay_rate = 0.8
    item3.apply_discount()
    assert item3.price == 2400
