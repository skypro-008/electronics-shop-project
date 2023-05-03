"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_first_homework(item):
    assert item.calculate_total_price() == 200000
    item.apply_discount()
    assert item.price == 10000
