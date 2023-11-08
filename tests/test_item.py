"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_for_test():
    return Item("Телевизор", 150000, 5)


def test_calculate_total_price(item_for_test):
    assert item_for_test.calculate_total_price() == 750000


def test_apply_discount(item_for_test):
    assert item_for_test.apply_discount() == 150000
