"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

def test_validate_data():
    """Тестирование класса Item"""
    item = Item('short', 10, 4)
    assert type(item.name) == str
    assert type(item.price) == int
    assert type(item.quantity) == int
    assert item.calculate_total_price() == 40
    item.pay_rate = 0.5
    item.apply_discount()
    item.price = 5.0