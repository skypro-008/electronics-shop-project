"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

tets_item = Item("apple", 50000, 10)


def test_Item_init():
    """Тест функции __init__ для класса Item"""
    assert tets_item.name == 'apple'
    assert tets_item.price == 50000
    assert tets_item.quantity == 10


def test_Item_calculate_total_price():
    """Тест функции calculate_total_price для класса Item"""
    assert tets_item.calculate_total_price() == 500000


def test_Item_apply_discount():
    """Тест функции apply_discount для класса Item"""
    Item.pay_rate = 0.5
    tets_item.apply_discount()
    assert tets_item.price == 25000
