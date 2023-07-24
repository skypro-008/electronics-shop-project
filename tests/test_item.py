"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def make_items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    return item1, item2


def test_calculate_total_price(make_items):
    """Тест функции расчета общей стоимости товара"""
    item1 = make_items[0]
    item2 = make_items[1]
    item1.calculate_total_price()
    item2.calculate_total_price()
    assert item1.total_price == 200000
    assert item2.total_price == 100000


def test_apply_discount(make_items):
    item1 = make_items[0]
    item2 = make_items[1]
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000
