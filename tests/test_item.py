"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    """
    Тест функции "calculate_total_price"
    На рассчёт общщей стоймости конкретного товара
    """
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000


def test_apply_discount():
    """
    Тест функции "apply_discount"
    на расссчёт стоимости на товар с учётом скидки
    """
    item = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    assert item.apply_discount() == 8000
