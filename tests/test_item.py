"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def product():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(product):
    assert product.calculate_total_price() == 200000


def test_apply_discount(product):
    product.apply_discount()
    assert product.calculate_total_price() == 18000.0
