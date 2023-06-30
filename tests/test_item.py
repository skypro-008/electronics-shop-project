"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item1():
    item1 = Item("Смартфон", 10000, 20)
    return item1


def test_calculate_total_price(item1):
    """
    При создании экземпляра класса со значениями name, price, quantity,
    функция calculate_total_price() вернет общую стоимость товара
    total_price = price * quantity
    """
    assert item1.calculate_total_price() == 200000
    # assert item2.calculate_total_price() == 100000


def test_apply_discount(item1):
    """
    При создании экземпляра класса со значениями name, price, quantity,
    функция apply_discount() вернет цену товара (price) с применением
    уровня цен, заданного по умолчанию в классе (pay_rate = 1.0) или
    заданного после переопределения (pay_rate = 0.5)
    """
    item1.apply_discount()
    assert item1.price == 10000

    Item.pay_rate = 0.5
    item1.apply_discount()

    assert item1.price == 5000.0
