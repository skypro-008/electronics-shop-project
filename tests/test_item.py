"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def tv():
    return Item("tv", 10000, 2)


def test_calculate_total_price(tv):
    tv.apply_discount()
    assert tv.calculate_total_price() == 20000.0


def test_apply_discount(tv):
    assert tv.apply_discount() is None
