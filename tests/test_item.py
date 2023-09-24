from src.item import Item


def test_calculate_total_price():
    test_item = Item('Товар', 200, 1)
    assert test_item.calculate_total_price() == 200


def test_apply_discount():
    test_item = Item('Товар', 200, 1)
    Item.pay_rate = 0.10
    assert test_item.apply_discount() == 20
