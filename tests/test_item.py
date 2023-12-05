"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item3():
    return Item("Телевизор", 15000, 5)


@pytest.fixture
def item4():
    return Item("Холодильник", 30000, 3)


def test_calculate_total_price(item3, item4):
    assert item3.calculate_total_price() == 75000
    assert item4.calculate_total_price() == 90000


def test_apply_discount(item3, item4):
    Item.pay_rate = 0.5
    item3.apply_discount()
    item4.apply_discount()
    assert item3.price == 7500
    assert item4.price == 15000
