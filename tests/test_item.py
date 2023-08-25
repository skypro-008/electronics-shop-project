"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item

def test_calculate_total_price(item1=None):
    assert 10000 * 20 == 200000
    assert item1.price * item1.quantity == item1.total_price


def test_apply_discount():
    assert 30000 * 1 == 30000
    assert 20000 * 0.8 == 16000


def test_calculate_total_price():
    with pytest.raises(TypeError):
        Item()