"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Фен", 3000, 20)
item2 = Item("Ноутбук", 25000, 2)


def test_Item():
    assert item1.calculate_total_price() == 60000
    assert item1.apply_discount() == None
    assert item2.name == "Ноутбук"
    assert item1.price == 3000
    assert item2.quantity == 2


def test_Item_prace():
    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 1500
