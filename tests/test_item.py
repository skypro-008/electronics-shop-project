"""Здесь надо написать тесты с использованием pytest для модуля item."""
# from src.item import calculate_total_price
import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item1):
    """Когда мы создаем экземпляр класса со значением item1, то calculate_total_price вернет нам результат"""
    assert item1.calculate_total_price() == 'Общая стоимость Смартфон в магазине составляет: 200000'


def test_apply_discount(item1):
    """Когда мы создаем экземпляр класса со значением item1, то calculate_total_price вернет нам результат"""
    assert item1.apply_discount() == 'Цена с учетом скидки 19% составляет 8000.0'


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


def test_calculate_total_price(item2):
    """Когда мы создаем экземпляр класса со значением item1, то calculate_total_price вернет нам результат"""
    assert item2.calculate_total_price() == 'Общая стоимость Ноутбук в магазине составляет: 100000'


def test_apply_discount(item2):
    """Когда мы создаем экземпляр класса со значением item1, то calculate_total_price вернет нам результат"""
    assert item2.apply_discount() == 'Цена с учетом скидки 19% составляет 16000.0'
