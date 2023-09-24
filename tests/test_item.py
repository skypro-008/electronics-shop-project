"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item

def test_calculate_total_price():
    """
    Тестирование функции calculate_total_price.

    """
    item1 = Item("Смартфон", 10000, 20)
    result = item1.calculate_total_price()
    assert result == 200000

def test_apply_discount():
    """
        Тестирование функции apply_discount.

    """
    item1 = Item("Смартфон", 10000, 20)
    result = item1.apply_discount()
    assert result == 10000


