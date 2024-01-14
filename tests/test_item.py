import pytest
from src.item import Item, InstantiateCSVError
import os


@pytest.fixture
def first_item():
    return Item("Изделие", 149.99, 2)


def test_apply_discount(first_item):
    first_item.apply_discount()
    assert first_item.price == 149.99


def test_calculate_total_price(first_item):
    assert first_item.calculate_total_price() == 299.98


@pytest.fixture
def sample_item():
    return Item("SampleItem", 49.99, 5)


def test_str_method(sample_item):
    assert str(sample_item) == "SampleItem"


def test_repr_method(sample_item):
    assert repr(sample_item) == "Item('SampleItem', 49.99, 5)"


def test_instantiate_from_csv():
    csv_data = "Phone,199.99,3\nLaptop,899.99,1\n"
    with open("test_items.csv", "w", encoding="utf-8") as csv_file:
        csv_file.write(csv_data)

    Item.instantiate_from_csv("test_items.csv")
    os.remove(csv_file.name)


def test_add_items():
    item1 = Item("Laptop", 1000, 2)
    item2 = Item("Tablet", 500, 3)
    result = item1 + item2
    assert result == 5


def test_add_invalid_type_raises_error():
    item1 = Item("Laptop", 1000, 2)
    invalid_type = "NotAnItemInstance"
    try:
        item1 + invalid_type
    except TypeError as e:
        assert str(e) == "Unsupported operation"