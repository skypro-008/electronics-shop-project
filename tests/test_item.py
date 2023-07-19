"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price(item):
    """
    Когда мы создаем экземляр класса с определенной ценой
    и количеством, должно вернутся произведение этих чисел.
    """
    assert Item.calculate_total_price(item) == 160000


def test_apply_discount(item):
    """
    Когда мы создаем экземляр класса с определенной ценой,
    должна вернутся эта цена без учета скидки.
    """
    assert Item.apply_discount(item) == 16000.0


def test_apply_discount_pay_rate(item):
    """
    Когда мы создаем экземляр класса с определенной ценой,
    указываем значение скидки, должна вернутся цена с учетом скидки.
    """
    item.pay_rate = 0.8
    assert Item.apply_discount(item) == 12800.0
