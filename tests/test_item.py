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
    total_price = initial_price * quantity

    assert item.calculate_total_price() == total_price


@pytest.mark.parametrize('pay_rate, initial_price, expected_price', [
    (0.85, 80_000, 68_000),
    (0.35, 120_000, 114_000),
    (0.5, 30_000, 15_000)
])
def test_apply_discount(item, pay_rate, initial_price, expected_price):
    item.pay_rate = pay_rate
    item.price = initial_price
    item.apply_discount()

    assert item.price == expected_price
