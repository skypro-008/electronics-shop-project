"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_item_creation():
    instance = Item("Смартфон", 10000, 20)
    assert instance.name == "Смартфон"
    assert instance.price == 10000
    assert instance.quantity == 20


def test_calculate_total_price():
    instance = Item("Телефон", 900, 10)
    assert isinstance(instance.calculate_total_price(), float) is True
    assert instance.calculate_total_price() == 9000


def test_apply_discount():
    instance = Item("Смартфон", 10000, 20)
    assert instance.pay_rate == 1.0

    Item.pay_rate = 0.7
    instance.apply_discount()
    assert instance.pay_rate == 0.7
    assert instance.price == 7000


