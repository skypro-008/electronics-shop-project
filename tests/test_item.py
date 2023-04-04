"""Здесь надо написать тесты с использованием pytest для модуля item."""
from electronics_shop.src.item import Item


def test_item():
    ex_item = Item("Смартфон", 10000, 20)
    assert ex_item.name == "Смартфон"
    assert ex_item.price == 10000
    assert ex_item.quantity == 20

def test_calculate_total_price():
    ex_item = Item("Ноутбук", 20000, 5)
    assert ex_item.calculate_total_price() == 100_000


def test_apply_discount():
    ex_item = Item("Ноутбук", 20000, 5)
    ex_item.pay_rate = 0.8
    ex_item.apply_discount()
    assert ex_item.price == 16_000
