"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def test_calculate_total_price():
    apple = Item('apple', 1, 10)
    assert apple.calculate_total_price() == 10

    orange = Item('orange', 2, 5)
    assert orange.calculate_total_price() == 10

    apple.apply_discount(0.9)
    assert apple.calculate_total_price() == 9

    orange.apply_discount(0.8)
    assert orange.calculate_total_price() == 8

def test_apply_discount():
    apple = Item('apple', 1, 10)
    assert apple.pay_rate == 1.0

    apple.apply_discount(0.9)
    assert apple.pay_rate == 0.9

    apple.apply_discount(0.8)
    assert apple.pay_rate == 0.8

