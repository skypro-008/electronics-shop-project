"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def test_item():
    # классы для проверки
    item1 = Item('Car', 250.0, 8)
    item2 = Item('Ball', 130.0, 3)

    # Проверка общей цены
    assert item1.calculate_total_price() == 2000.0
    assert item2.calculate_total_price() == 390.0

    # Проверка скидки
    item1.pay_rate = 10.0
    item1.apply_discount()
    assert item1.price == 2500.0

    item2.pay_rate = 20.0
    item2.apply_discount()
    assert item2.price == 2600.0

    # Проверка списка экзепляров
    assert Item.all == [item1, item2]