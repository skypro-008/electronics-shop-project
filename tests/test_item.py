"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_test():
    return Item("Телевизор", 150000, 5)


def calculate_total_price():
    assert item_test.calculate_total_price() == 750000


def apply_discount():
    assert item_test.apply_discount() == 150000
