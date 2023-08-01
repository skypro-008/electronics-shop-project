"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_item():
    return Item("Смартфон", 10000, 20)


def test_fix_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 200000


def test_fix_change_pay_rate(test_item):
    assert test_item.pay_rate == 0.8


def test_fix_is_none_apply_discount(test_item):
    assert test_item.apply_discount() is None


def test_fix_apply_discount(test_item):
    assert int(test_item.price * test_item.pay_rate) == 8000


def test_fix_pay_rate(test_item):
    assert test_item.pay_rate == 0.8


item1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_is_none_apply_discount():
    assert item1.apply_discount() is None


def test_apply_discount():
    assert int(item1.price * item1.pay_rate) == 8000


Item.pay_rate = 0.8


def test_pay_rate():
    assert item1.pay_rate == 0.8
