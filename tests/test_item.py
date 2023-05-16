"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def item():
    return Item("Принтер Epson L121 (C11CD76414)", 5299, 8)


def test_create_float(item):
    assert item.name == "Принтер Epson L121 (C11CD76414)"
    assert item.price == float(5299)
    assert item.quantity == 8
    assert item.pay_rate == 1.0


def test_create_int(item):
    assert item.name == "Принтер Epson L121 (C11CD76414)"
    assert item.price == 5299
    assert item.quantity == 8
    assert item.pay_rate == 1.0


def test_create_incorrect():
    with pytest.raises(ValueError):
        item = Item(8, 5299, 8)

    with pytest.raises(ValueError):
        item = Item("Принтер Epson L121 (C11CD76414)", "5299", 8)

    with pytest.raises(ValueError):
        item = Item("Принтер Epson L121 (C11CD76414)", 5299, "8")


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 5299 * 8


def test_calculate_total_price_errors(item):
    item.price = "5299"
    item.quantity = "8"
    with pytest.raises(ValueError):
        assert item.calculate_total_price()

    item.price = "5299"
    item.quantity = 8
    with pytest.raises(ValueError):
        assert item.calculate_total_price()

    item.price = 5299.0
    item.quantity = "8"
    with pytest.raises(ValueError):
        assert item.calculate_total_price()


def test_apply_discount(item):
    item.pay_rate = 0.85
    item.price = 6000.0
    item.apply_discount()
    assert item.price == 0.85 * 6000.0


def test_apply_discount_incorrect(item):
    item.pay_rate = 85
    item.price = 6000.0
    with pytest.raises(ValueError):
        item.apply_discount()

    item.pay_rate = 0.85
    item.price = "6000.0"
    with pytest.raises(ValueError):
        item.apply_discount()

    item.pay_rate = "1.0"
    item.price = 6000.0
    with pytest.raises(ValueError):
        item.apply_discount()
