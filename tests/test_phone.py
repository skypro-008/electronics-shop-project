import pytest
from src.phone import Phone
from src.item import Item

@pytest.fixture
def phone_data():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    return phone

@pytest.fixture
def item_data():
    item = Item("Смартфон", 10000, 20)
    return item


def test_item_init(phone_data):
    assert str(phone_data) == 'iPhone 14'
    assert repr(phone_data) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone_data.name == 'iPhone 14'
    assert phone_data.price == 120000
    assert phone_data.quantity == 5
    assert phone_data.number_of_sim == 2

def test_item_add(phone_data, item_data):
    assert item_data + phone_data == 25
    assert phone_data + phone_data == 10