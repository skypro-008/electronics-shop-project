"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def first_item():
    return Item("Изделие", 149.99, 2)


def test_apply_discount(first_item):
    first_item.apply_discount()
    assert first_item.price == 149.99


def test_calculate_total_price(first_item):
    assert first_item.calculate_total_price() == 299.98
