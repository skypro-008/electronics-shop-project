"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture()
def test_data_one():
    return "Ноутбук", 20000, 5


@pytest.fixture()
def test_data_two():
    return "Смартфон", 10000, 20


@pytest.fixture()
def test_data_there():
    return "Насос", 5000, 10


def test_item_py_one(test_data_one):
    class_exemplar = Item(*test_data_one)
    assert class_exemplar.name == "Ноутбук"
    assert class_exemplar.price == 20000
    assert class_exemplar.quantity == 5
    assert class_exemplar.calculate_total_price() == 100000
    class_exemplar.pay_rate = 0.8
    class_exemplar.apply_discount()
    assert class_exemplar.price == 16000


def test_item_py_two(test_data_two):
    class_exemplar = Item(*test_data_two)
    assert class_exemplar.name == "Смартфон"
    assert class_exemplar.price == 10000
    assert class_exemplar.quantity == 20
    assert class_exemplar.calculate_total_price() == 200000
    class_exemplar.pay_rate = 0.8
    class_exemplar.apply_discount()
    assert class_exemplar.price == 8000


def test_item_py_there(test_data_there):
    class_exemplar = Item(*test_data_there)
    assert class_exemplar.name == "Насос"
    assert class_exemplar.price == 5000
    assert class_exemplar.quantity == 10
    assert class_exemplar.calculate_total_price() == 50000
    class_exemplar.pay_rate = 0.8
    class_exemplar.apply_discount()
    assert class_exemplar.price == 4000


def test_item_py_four(test_data_one):
    class_exemplar = Item(*test_data_one)
    class_exemplar.name = 'Суперсмартфон'
    assert class_exemplar.name == 'Суперсмартфон'
    class_exemplar.name = 'Телефон'
    assert class_exemplar.name == 'Телефон'


def test_item_py_five():
    Item.instantiate_from_csv('src/items.csv')
    # assert len(Item.all) == 5


def test_item_py_six():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
