"""Здесь надо написать тесты с использованием pytest для модуля item."""


from src.item import Item


test_item = Item("Смартфон", 10000, 20)
test_item_2 = Item("Ноутбук", 20000, 5)

# TestCase#1 Item.__init__
assert test_item.price == 10000
assert test_item.name == "Смартфон"
assert test_item.quantity == 20
assert Item.all == [test_item, test_item_2]

# TestCase#2 Item.calculate_total_price
assert test_item.calculate_total_price() == 200000
assert test_item_2.calculate_total_price() == 100000

# TestCase#3 Item.apply_discount
assert test_item.apply_discount() == None
assert test_item.price == 10000
test_item.pay_rate = 0.8
test_item.apply_discount()
assert test_item.price == 8000

