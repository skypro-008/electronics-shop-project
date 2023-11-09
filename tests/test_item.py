"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

test_item = Item("чай", 100, 20000)


def test_calculate_total_price():

    assert test_item.calculate_total_price() == 2000000


def test_apply_discount():

    test_item.apply_discount()
    assert test_item.price == 100

    Item.pay_rate = 2.0
    test_item.apply_discount()
    assert test_item.price == 200