from src.item import Item

def test_item():
    item = Item('test', 10000, 10)

    # TestCase #1 name
    assert item.name == "test"

    # TestCase #2 price
    assert item.price == 10000

    # TestCase #3 quantity
    assert item.quantity == 10

    # TestCase #4 calculate_total_price
    assert item.calculate_total_price() == 100000

    # TestCase #5 apply_discount
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000





