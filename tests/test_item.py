"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_calculate_total_price():
    test_price = 10000
    test_quantity = 5
    assert Item.calculate_total_price(test_price, test_quantity) == 50000


def test_instantiate_from_csv():
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_apply_discount():
    test_price_1 = 10000
    test_pay_rate_1 = 0.85
    assert Item.apply_discount(test_price_1, test_pay_rate_1) == 8500
    test_price_1 = 10000
    test_pay_rate_1 = 0
    assert Item.apply_discount(test_price_1, test_pay_rate_1) == None


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
