"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def one_item():
    return Item('Булка', 40, 7)


def test_item_init():
    bread = one_item()
    assert bread.name == 'Булка'


def test_item_apply_discount():
    bread = one_item()
    bread.pay_rate = 0.5
    bread.apply_discount()
    assert bread.pay_rate == 20


def test_item_calculate_total_price():
    bread = one_item()
    assert bread.calculate_total_price() == 280

