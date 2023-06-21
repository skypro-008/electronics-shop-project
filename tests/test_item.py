"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

item1 = Item("Смартфон", 10000, 20)

def test_Item():
    assert item1.name == "Смартфон"
    assert item1.price == 10000

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    total_price = item1.calculate_total_price() == 200000

