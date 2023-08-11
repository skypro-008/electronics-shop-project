"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

def test_calculate_total_price():
    item1 = Item("Ноут", 10000, 2)
    item2 = Item("Смарт", 5000, 10)

    assert item1.name == "Ноут"
    assert item1.price == 10000
    assert item1.quantity == 2

    assert item1.calculate_total_price() == 20000
    assert item2.calculate_total_price() == 50000


def test_apply_discount():
    item1 = Item("Ноут", 10000, 2)
    item2 = Item("Смарт", 5000, 10)

    assert item1.price == 10000
    assert item2.price == 5000

    Item.pay_rate = 0.5
    item1.apply_discount()
    item2.apply_discount()

    assert item1.price == 5000
    assert item2.price == 2500



