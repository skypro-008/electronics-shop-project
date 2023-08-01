"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def make_items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    return item1, item2


def test_calculate_total_price(make_items):
    """Тест функции расчета общей стоимости товара"""
    item1 = make_items[0]
    item2 = make_items[1]
    item1.calculate_total_price()
    item2.calculate_total_price()
    assert item1.total_price == 200000
    assert item2.total_price == 100000


def test_apply_discount(make_items):
    item1 = make_items[0]
    item2 = make_items[1]
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000


def test_add_element(make_items):
    item1 = make_items[0]
    item2 = make_items[1]
    assert len(Item.all) == 2


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_name(make_items):
    item1 = make_items[0]
    item2 = make_items[1]
    isinstance(item1.name, str)
    isinstance(item2.name, str)
    assert item1.name == "Смартфон"
    item2.name = 'СуперСмартфон'
    assert item2.name == 'СуперСмарт'


def test_string_to_number():
    assert Item.string_to_number('5') == 5


def test_repr(make_items):
    item1 = make_items[0]
    item2 = make_items[1]
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Ноутбук', 20000, 5)"


def test_str(make_items):
    item1 = make_items[0]
    item2 = make_items[1]
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Ноутбук'
