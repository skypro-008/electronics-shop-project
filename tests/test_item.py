"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 200_000


def test_apply_discount(test_item):
    Item.pay_rate = 0.5
    test_item.apply_discount()
    assert test_item.price == 5000


def test_name_getter(test_item):
    assert test_item.name == "Смартфон"

