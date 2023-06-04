import pytest

from src.item import Item


class TestItem:
    item = Item('iPhone 14 Pro Max', 100000, 50)

    def test_calculate_total_price(self):
        assert self.item.calculate_total_price() == 5000000

    def test_apply_discount(self):
        self.item.pay_rate = 0.8
        self.item.apply_discount()
        assert self.item.calculate_total_price() == 4000000.0
