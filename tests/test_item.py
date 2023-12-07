"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def test_calculate_total_price():
    assert Item("Смартфон", 10000, 20).calculate_total_price() == 200000

def test_apply_discount():
    item = Item("Смартфон", 10000, 20)
    item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 5000








