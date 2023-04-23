from src.item import Item

item1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    assert Item.calculate_total_price(item1) == 100000.0
