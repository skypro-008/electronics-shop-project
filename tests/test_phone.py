from src.item import Item
from src.phone import Phone


def test_phone_init():
    phone_1 = Phone('test_phone', 50000, 10, 2)
    assert phone_1.name == 'test_phone'
    assert phone_1.price == 50000
    assert phone_1.quantity == 10
    assert phone_1.number_of_sim == 2
