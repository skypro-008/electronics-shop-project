"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

def test_item():
    assert item1.price * item1.pay_rate == 10000.0
    assert item2.name == "Ноутбук"
