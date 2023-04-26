"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
item1 = Item("name", 10.0, 1000)


def test_Item___init__():
    assert item1.get_name() == "name"
    assert len(Item.all) == 1
    item1.pay_rate = 0.9
    item1.apply_discount()
    assert item1.price == 9.0
    assert item1.calculate_total_price() == 9000.0

def test_strtonum():
    assert item1.string_to_number("5.0") == 5
    assert item1.string_to_number("2") == 2

def test_Item_repr_str():
    assert repr(item1) == "Item('name', 9.0, 1000)"
    assert str(item1) == "name"