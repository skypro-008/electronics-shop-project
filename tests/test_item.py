"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src import item


def item_item():
    return item.Item("Смартфон", 10000, 20)


def test___init__():
    assert item_item().__init__("Смартфон", 10000, 20) is None


def test_calculate_total_price():
    assert item_item().calculate_total_price() == 200000


def test_apply_discount():
    assert item_item().apply_discount() is None


if __name__ == '__main__':
    pytest.main()
