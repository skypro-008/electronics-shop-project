""" Item Class testing module"""
import pytest

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
