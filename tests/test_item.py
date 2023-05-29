"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item


@pytest.fixture
def smartphone():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(smartphone):
    """Рассчитывает общую стоимость товара Смартфон в магазине."""

    assert smartphone.calculate_total_price() == 200000


def test_apply_discount(smartphone):
    """Вводим скидку 50%, должно вернуть = price * 0.5"""

    Item.pay_rate = 0.5
    assert smartphone.apply_discount() == 5000
