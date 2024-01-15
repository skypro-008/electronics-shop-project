import pytest
from src.item import Item


def test_valid_parameters_no_errors():
    item = Item("Item 1", 100, 1)
    assert item.name == "Item 1"
    assert item.price == 100
    assert item.quantity == 1
    assert item in Item.all


def test_calculate_total_price():
    item = Item("Item 2", 50, 2)
    total_price = item.calculate_total_price()
    assert total_price == 100


def test_apply_discount_valid_discount():
    item = Item("Item 3", 100, 1)
    item.pay_rate = 0.1
    item.apply_discount()
    assert item.price == 10


def test_empty_name_raises_value_error():
    with pytest.raises(ValueError):
        item = Item("", 100, 1)


def test_negative_quantity_raises_value_error():
    with pytest.raises(ValueError):
        item = Item("Item 4", 100, -1)


def test_zero_or_negative_price_raises_value_error():
    with pytest.raises(ValueError):
        item = Item("Item 5", -100, 1)
