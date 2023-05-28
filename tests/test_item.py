"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import calculate_total_price, apply_discount


def test_calculate_total_price():
    test_price_1 = 10000
    test_quantity_1 = 5
    assert calculate_total_price(test_price_1, test_quantity_1) == 50000


def test_apply_discount():
    test_price_1 = 10000
    test_Item_pay_rate_1 = 0.85
    assert apply_discount(test_price_1, test_Item_pay_rate_1) == 8500
    test_price_1 = 10000
    test_Item_pay_rate_1 = 0
    assert apply_discount(test_price_1, test_Item_pay_rate_1) == None
