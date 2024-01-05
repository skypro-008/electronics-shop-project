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
    (0.95, 120_000, 114_000),
    (0.5, 30_000, 15_000)
])
def test_apply_discount(item, pay_rate, initial_price, expected_price):
    item.pay_rate = pay_rate
    item.price = initial_price
    item.apply_discount()

    assert item.price == expected_price


@pytest.mark.parametrize('name, result_name', [
    ('Laptop Top-Top', 'Laptop Top'),
    ('IPhone X-Men Pro', 'IPhone X-M'),
    ('Smart Lamp But Not You', 'Smart Lamp'),
    ('AppleWatchingYou', 'AppleWatch'),
    ('Lenovo 4Vova', 'Lenovo 4Vo'),
    ('This Is 10', 'This Is 10'),
    ('Only 1', 'Only 1')
])
def test_name(item: object, name: str, result_name: str):
    item.name = name

    assert item.name == result_name


@pytest.mark.parametrize('string_value, int_result', [
    ('3.5', 3),
    ('8.2', 8),
    ('4.0', 4),
    ('9', 9)
])
def test_string_to_number(item, string_value, int_result):
    try:
        int_result = int(string_value)
    except ValueError:
        int_result = int(float(string_value))

    assert item.string_to_number(string_value) == int_result
