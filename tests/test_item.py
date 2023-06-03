"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.mark.parametrize('price, quantity, expected', [
    (10000, 20, 200000),
    (20000, 5, 100000)
])
def test_calculate_total_price(price, quantity, expected):
    assert calculate_total_price(price, quantity) == expected


def test_apply_discount():
    assert apply_discount() == 10000
    assert apply_discount() == 20000
