"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

Item.pay_rate = 0.85
item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
item3 = Item("Фотоаппарат", 50000, 0)


def test_calculate_total_price():
    """
    Тест метода, вычисляющего общую цену товара
    """
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000
    assert item3.calculate_total_price() == "Товар закончился"


def test_apply_discount():
    """
    Тест метода, применяющего скидку
    """
    assert item1.apply_discount() == 8500
    assert item2.apply_discount() == 17000
    assert item3.apply_discount() == 42500
