"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

data = Item("Смартфон", 10000, 20)

def test_calculate_total_price():
    """проверяет правильность метода, который рассчитывает общую стоимость конкретного товара в магазине"""
    assert data.calculate_total_price() == 200000
    assert data.quantity ==20


def test_apply_discount():
    """Проверяет правильность метода, который применяет установленную скидку для конкретного товара"""
    data.pay_rate = 0.8
    data.apply_discount()
    assert data.price == 8000


