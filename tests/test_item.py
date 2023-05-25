""" Item Class testing module"""
import csv

import pytest

from src.item import Item
from tests.conftest import item_class


class TestItem:
    """
    Item class testing Class
    """
    items = item_class()

    @pytest.mark.parametrize(
        "item, expected", [
            (items[0], 51017.0),
            (items[1], 22712.5)
        ]
    )
    def test_calculate_total_price(self, item, expected):
        """
        Test the calculate_total_price() method of the item.

        Args:
            item: An item object to calculate the total price.
            expected: The expected total price of the item.

        Returns:
            None.
        """
        assert item.calculate_total_price() == expected

    @pytest.mark.parametrize(
        "item, expected", [
            (items[0], 2250.75),
            (items[1], 493.75)
        ]
    )
    def test_apply_discount(self, item, expected):
        """
        Test the apply_discount() method of the item.

        Args:
            item: An item object to apply a discount to.
            expected: The expected price of the item after
            applying the discount.

        Returns:
            None.
        """
        item.apply_discount()
        assert item.price == expected

    @pytest.mark.parametrize(
        "item, expected", [
            (items[0], 2),
            (items[1], 2)
        ]
    )
    def test_all(self, item, expected):
        """
        Test the all attribute of the item.

        Args:
            item: An item object to access the all attribute.
            expected: The expected length of the all attribute.

        Returns:
            None.
        """
        assert len(item.all) == expected


def test_name_getter(test_item):
    """
    Test the getter for the name property of Item.

    Args:
        test_item (fixture): Fixture that provides instances
        of Item for testing.

    Returns:
        None
    """
    assert test_item[0].name == 'Test1'
    assert test_item[1].name == 'Test2'


def test_name_setter(test_item):
    """
    Test the setter for the name property of Item.

    Args:
        test_item (fixture): Fixture that provides instances of
        Item for testing.

    Returns:
        None
    """
    test_item[0].name = 'Test10'
    assert test_item[0].name == 'Test10'
    test_item[1].name = 'Test20'
    assert test_item[1].name == 'Test20'
    with pytest.raises(ValueError):
        test_item[1].name = 'СуперСмартфон'


def test_instantiate_from_csv(monkeypatch):
    """
    Test the instantiate_from_csv method of Item.

    Args:
        monkeypatch: pytest fixture to modify the behavior of
        functions temporarily.

    Returns:
        None
    """
    csv_data = [
        {'name': 'Product 1', 'price': '10', 'quantity': '5'},
        {'name': 'Product 2', 'price': '20', 'quantity': '3'},
        {'name': 'Product 3', 'price': '15', 'quantity': '8'},
    ]

    def mock_open(*args, **kwargs):  # pylint: disable=W0613
        return csv_data

    monkeypatch.setattr(csv, 'DictReader', mock_open)

    Item.instantiate_from_csv()


def test_string_to_number():
    """
    Test the string_to_number method of Item.

    Returns:
        None
    """
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('20') == 20
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('0') == 0
    assert Item.string_to_number('-10') == -10
