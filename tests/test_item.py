"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item():
    item1 = Item("Ноут", "20.0", 10)

    assert item1.name == "Нт"
    assert item1.price == "20.0"
    assert item1.quantity == 10
