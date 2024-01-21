"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item1 = Item("Картошка", 120, 100)
    assert item1.calculate_total_price() == 12000

    item2 = Item("Морковка", 40, 200)
    Item.pay_rate = 0.8
    item2.apply_discount()
    assert item2.calculate_total_price() == 6400

    item3 = Item("Смартфон", 10000, 20)
    item4 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    item3.apply_discount()
    assert item3.price == 8000.0
    assert item4.price == 20000