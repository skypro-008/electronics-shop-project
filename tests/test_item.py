"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def exemple():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(exemple):
    assert exemple.calculate_total_price() == 10000


def test_apply_discount(exemple):
    exemple.pay_rate = 0.8
    exemple.apply_discount()
    assert exemple.price == 8000
