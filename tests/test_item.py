"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def product():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(product):
    assert product.calculate_total_price() == 200000


def test_apply_discount(product):
    product.apply_discount()
    assert product.calculate_total_price() == 180000.0


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name(product):
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5