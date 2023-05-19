"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest as pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("item1", 10.0, 5)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50.0


def test_apply_discount(item):
    item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 9.0


def test_all_items():
    if __name__ == "__main__":
        item1 = Item("item1", 10, 5)
        item2 = Item("item2", 20, 2)
