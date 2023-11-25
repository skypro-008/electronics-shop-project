import pytest

from src.item import Item


@pytest.fixture
def test_data():
    item_1 = Item("Смартфон", 10000, 5)
    item_2 = Item("Ноутбук", 25000, 3)
    item_1.pay_rate = 0.8
    item_2.pay_rate = 0.95
    return item_1, item_2


def test_valid_item(test_data):
    assert test_data[0].name == "Смартфон"
    assert test_data[0].price == 10000
    assert test_data[0].quantity == 5

    assert test_data[1].name == "Ноутбук"
    assert test_data[1].price == 25000
    assert test_data[1].quantity == 3


def test_calculate_total_price(test_data):
    assert test_data[0].calculate_total_price() == 50000
    assert test_data[1].calculate_total_price() == 75000


def test_apply_discount(test_data):
    test_data[0].apply_discount()
    assert test_data[0].price == 8000
    test_data[1].apply_discount()
    assert test_data[1].price == 23750
