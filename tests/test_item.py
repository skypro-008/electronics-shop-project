import pytest
from src import item


class TestItem():
    """Тест для класса Item"""

    def test_calculate_total_price_1(self):
        """
        Проверяет произведение цена на количество товаров
        """
        assert item.Item("Смартфон", 50000, 10).calculate_total_price() == 500000


    def test_calculate_total_price_2(self):
        """
        Проверяет тип значения функции calculate_total_price(), int
        """
        assert isinstance(item.Item("Смартфон", 50000, 10).calculate_total_price(), int)


    def test_apply_discount(self):
        """
        Проверяет правильность расчета скидки
        """
        item.Item.pay_rate = 2.0
        assert item.Item("Смартфон", 50000, 10).apply_discount() == 100000

