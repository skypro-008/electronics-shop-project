"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

# TestCase#1 TotalPrise
item1 = Item('product1', 10000, 2)
assert item1.calculate_total_price() == 20000

# TestCase#2  ApplyDiscount
item1 = Item('product1', 20000, 2)
item1.apply_discount()
assert item1.calculate_total_price() == 40000
assert item1.apply_discount() is None



