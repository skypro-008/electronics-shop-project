"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10_000, 20)


def test_init(item1):
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20
    assert Item.all[0] == item1


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200_000


def test_apply_discount(item1):
    old_price = item1.price
    item1.apply_discount()
    assert item1.price == old_price * Item.pay_rate


def test_class_attribute(item1):
    assert isinstance(Item.pay_rate, float)
    assert isinstance(Item.all, list)
