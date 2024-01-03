"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest


@pytest.mark.parametrize('initial_price, quantity, total_price', [
    (50_000, 3, 150_000),
    (70_000, 2, 140_000),
    (30_000, 1, 30_000)
])
def test_calculate_total_price(item, initial_price, quantity, total_price):
    item.price = initial_price
    item.quantity = quantity

    assert item.calculate_total_price() == total_price
