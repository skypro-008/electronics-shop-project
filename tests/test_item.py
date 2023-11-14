"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)

def test_class_Item_name1(item1):
    assert item1.name == 'Смартфон'

def test_class_Item_name2(item1):
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'

def test_class_Item_price(item1):
    assert item1.price == 10000


def test_class_Item_quantity(item1):
    assert item1.quantity == 20


def test_class_Item_pay_rate(item1):
    assert item1.pay_rate == 1.0


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    item1.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000


@pytest.mark.parametrize('string, expected_result', [('5', 5),
                                                     ('5.0', 5),
                                                     ('5.5', 5)])
def test_string_to_number(string, expected_result):
    assert Item.string_to_number(string) == expected_result


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5

