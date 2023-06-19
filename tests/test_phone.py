from src.item import Item
from src.phone import Phone

phone_1 = Phone('test_phone', 50000, 10, 2)
item_1 = Item('test_item', 10000, 7)


def test_phone_init():
    assert phone_1.name == 'test_phone'
    assert phone_1.price == 50000
    assert phone_1.quantity == 10
    assert phone_1.number_of_sim == 2


def test_phone_add():
    assert item_1 + phone_1 == 17
    assert phone_1 + phone_1 == 20
    assert phone_1 + 6 is None

