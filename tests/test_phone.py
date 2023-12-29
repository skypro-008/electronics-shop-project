import unittest

from src.phone import Phone
from src.item import Item


class TestPhone(unittest.TestCase):
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)

    def test_repr(self):
        assert repr(self.phone1) == "Item('Смартфон', 10000, 20)"

    def test_add(self):
        assert self.item1 + self.phone1 == 25
        assert self.phone1 + self.phone1 == 10

    def test_number_of_sim(self):
        with self.assertRaises(ValueError):
            self.phone1.number_of_sim = 0
