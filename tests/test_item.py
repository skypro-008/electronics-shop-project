"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def test_item():
    return Item(name="Phone", price=1000, quantity=10)


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 10000


def test_apply_discount(test_item):
    test_item.pay_rate = 0.8
    test_item.apply_discount()
    assert 1000 * test_item.pay_rate == test_item.price


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.2") == 5
    assert Item.string_to_number("5.0") == 5


def test_name(test_item):
    item1 = test_item
    item1.name = "WIN"
    assert item1.name == "WIN"
    item1.name = "012345678910"
    assert len(item1.name) == 10
    assert item1.name == "0123456789"

