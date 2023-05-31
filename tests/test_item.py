"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import calculate_total_price, apply_discount, string_to_number, name, instantiate_from_csv


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

def test_name():
    test_name_1 = "Телефон"
    assert name(test_name_1) == "Телефон"
    test_name_2 = "СуперСмартфон"
    assert name(test_name_2) == "Длина наименования товара превышает 10 символов."
def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_findLen():
    test_name = 'Anna'
    assert test_findLen(test_name) == 4