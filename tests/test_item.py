import pytest

from tests.conftest import item_class


class TestItem:
    items = item_class()

    @pytest.mark.parametrize(
        "item, expected", [
            (items[0], 51017.0),
            (items[1], 22712.5)
        ]
    )
    def test_calculate_total_price(self, item, expected):
        assert item.calculate_total_price() == expected

    @pytest.mark.parametrize(
        "item, expected", [
            (items[0], 2250.75),
            (items[1], 493.75)
        ]
    )
    def test_apply_discount(self, item, expected):
        item.apply_discount()
        assert item.price == expected

    @pytest.mark.parametrize(
        "item, expected", [
            (items[0], 2),
            (items[1], 2)
        ]
    )
    def test_all(self, item, expected):
        assert len(item.all) == expected
