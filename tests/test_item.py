"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def product_list_1():
    return Item("Пулемет", 25000, 5)


def test_calculate_total_price(product_list_1):
    assert product_list_1.calculate_total_price() == 125000


def test_apply_discount(product_list_1):
    Item.pay_rate = 0.5
    product_list_1.apply_discount()
    assert product_list_1.price == 12500
