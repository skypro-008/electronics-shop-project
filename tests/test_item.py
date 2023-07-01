"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_init_item(test_case_item1):
    """Тестирует инициализацию"""
    assert test_case_item1.name == "Смартфон"
    assert test_case_item1.price == 10000
    assert test_case_item1.quantity == 20
    assert len(test_case_item1.all) == 1
    assert type(test_case_item1.all[0]) == Item


def test_calculate_total_price(test_case_item1, test_case_item2):
    """Тестирует вычисление общей стоимости"""
    assert test_case_item1.calculate_total_price() == 200000
    assert test_case_item2.calculate_total_price() == 100000


def test_apply_discount(test_case_item1, test_case_item2):
    """Тестирует применение скидки"""
    Item.pay_rate = 0.8
    test_case_item1.apply_discount()

    assert test_case_item1.price == 8000.0
    assert test_case_item2.price == 20000

