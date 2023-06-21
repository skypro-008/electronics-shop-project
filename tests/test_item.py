"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


assert Item == Item("Сковородка", 1, 1)

assert 20000 * Item.pay_rate == Item.price

assert Item.price == 80000
