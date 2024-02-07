"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

data = Item("Смартфон", 10000, 20)


def test_calculate():
    """
    Тестируем рассчет общей стоимость конкретного товара в магазине.
    """
    assert data.calculate_total_price() == 200000


def test_apply_discount():
    """
    Проверяем действие установленной скидки для конкретного товара.
    """
    data.pay_rate = 0.7
    data.apply_discount()
    assert data.price == 7000
