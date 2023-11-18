"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, filename


@pytest.fixture
def test_class():
    item = Item(name='test', price=5, quantity=10, )
    return item


def test_calculate_total_price(test_class):
    assert test_class.calculate_total_price() == 50


def test_apply_discount(test_class):
    assert test_class.apply_discount() == 5


def test_name_setter(test_class):
    test_class.name = 'qwertyuiopasd'
    assert test_class.name == 'qwertyuiopasd'


def test_instantiate_from_csv(test_class):
    test_class.instantiate_from_csv(filename)
    assert len(test_class.all) == 5


def test_string_to_number(test_class):
    assert test_class.string_to_number('15.0') == 15


def test_str(test_class):
    assert str(test_class) == 'test'


def test_repr(test_class):
    assert repr(test_class) == "Item('test', 5, 10)"


def test_add(test_class):
    item1 = Item('Sly', 50000, 30)
    assert test_class.quantity + item1.quantity == 40
