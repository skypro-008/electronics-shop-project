"""Здесь надо написать тесты с использованием pytest для модуля item."""


from src.item import Item


# TestCase#1
test_item = Item("Смартфон", 10000, 20)
assert test_item.calculate_total_price() == 10000
test_item_2 = Item("Ноутбук", 20000, 5)
assert test_item_2.calculate_total_price() == 20000