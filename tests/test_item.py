"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

test_item = Item('Test', price=100, quantity=5)

def test_init():
    assert list(vars(test_item).values()) == ['Test', 100, 5]

def test_calculate_total_price():
    assert test_item.calculate_total_price() == 500

def test_apply_discount():
    Item.pay_rate = 0.9
    test_item.apply_discount()
    assert test_item.price == 90

