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


@pytest.mark.parametrize("expected_name", ["John", "Alice"])
def test_name(expected_name):
    # Create an instance of the class and set the name
    obj = Item()
    obj.name = expected_name
    # Assert that the property returns the expected value
    assert obj.name == expected_name


def test_string_to_number():
    obj = Item()
    assert obj.string_to_number("1.5") == 1
    assert obj.string_to_number("3.7") == 3
    assert obj.string_to_number("10.2") == 10
    assert obj.string_to_number("0.8") == 0


import pytest


@pytest.mark.parametrize(
    "csv_path, expected_length, expected_name, expected_price",
    [
        ("src/items.csv", 5, "Смартфон", 100),
    ],
)
def test_instantiate_from_csv(csv_path, expected_length, expected_name, expected_price):
    Item.all.clear()
    Item.instantiate_from_csv(csv_path)
    assert len(Item.all) == expected_length
    assert Item.all[0].name == expected_name
    assert Item.all[0].price == expected_price
