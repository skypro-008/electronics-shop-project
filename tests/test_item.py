"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture()
def item():
    return Item("Смартфон", 10000, 20)


class TestItem:

    def test_init_item(self, item):
        assert item.price == 10000
        assert item.name == "Смартфон"
        assert item.quantity == 20
        assert item.all == [item]

    def test_calculate_total_price(self, item):
        assert isinstance(item.calculate_total_price(), int)
        assert item.calculate_total_price() == 200000

    def test_apply_discount(self, item):
        item.pay_rate = 0.8
        item.apply_discount()
        assert item.price == 8000.0

    def test_string_to_number(self, item):
        assert Item.string_to_number('5') == 5
        assert Item.string_to_number('5.0') == 5
        assert Item.string_to_number('5.5') == 5

    def test_repr_item(self, item):
        assert repr(item) == "Item('Смартфон', 10000, 20)"
        assert str(item) == 'Смартфон'