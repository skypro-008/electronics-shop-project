import pytest
from src import item


class TestItem:
    """Тесты для класса Item"""

    def test_calculate_total_price_1(self):
        """
        Проверяет произведение цены на количество товаров
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

    def test_instantiate_from_csv_1(self):
        """
        Проверяет количество позиций (ассортимента) товаров
        """

        item.Item.instantiate_from_csv()
        assert len(item.Item.all) == 5

    def test_instantiate_from_csv_2(self):
        """
        Проверяет название товара
        """

        item.Item.instantiate_from_csv()
        name_test = item.Item.all[2]
        assert name_test.name == 'Кабель'

    def test_instantiate_from_csv_3(self):
        """
        Проверяет стоимость товара
        """

        item.Item.instantiate_from_csv()
        price_test = item.Item.all[3]
        assert price_test.price == 50

    def test_instantiate_from_csv_4(self):
        """
        Проверяет количество товара
        """

        item.Item.instantiate_from_csv()
        quantity_test = item.Item.all[4]
        assert quantity_test.quantity == 5

    def test_string_to_number(self):
        """
        Проверяет правильность преобразования числа-строки в число без точки
        """
        assert item.Item.string_to_number('70') == 70
        assert item.Item.string_to_number('76.0') == 76
        assert item.Item.string_to_number('33.5') == 33
