"""Здесь надо написать тесты с использованием pytest для модуля item."""

from pytest import fixture

from src.item import Item


@fixture
def item():
    return Item("Смартфон", 10000, 20)

def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000

def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 10000

