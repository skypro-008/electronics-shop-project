"""Здесь надо написать тесты с использованием pytest для модуля item."""
import unittest
from src import item
class TestItem(unittest.TestCase):
    """Тест для класса Item"""

    def test_calculate_total_price(self):
        item1 = item.Item("Смартфон", 10000, 20)
        self.assertEqual(item1.calculate_total_price(), 200000)


if __name__ == '__main__':
    unittest.main()