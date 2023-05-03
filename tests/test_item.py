"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_hm_1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(test_hm_1):
    assert test_hm_1.calculate_total_price() == 200000


