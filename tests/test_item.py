"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    # проверяем, что метод calculate_total_price() возвращает правильную общую стоимость
    item1 = Item("Телефон", 10000, 20)
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    # экземпляр класса item, проверяем скидку и что цена уменьшилась на 20%
    item = Item("Телефон", 10000.0, 2)
    item.apply_discount()
    assert item.price == 8000.0
