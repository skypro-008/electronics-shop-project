"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone

@pytest.fixture
def item_test():
    return Item("Миксер", 10.2, 15)

@pytest.fixture
def phone_test():
    return Phone("Хонор", 100.1, 5, 1)

def test_item_init(item_test):

    assert item_test.name == "Миксер"
    assert item_test.price == 10.2
    assert item_test.quantity == 15


def test_item_calculate_total_price (item_test):

    assert item_test.calculate_total_price() == 153


def test_item_apply_discount (item_test):

    Item.pay_rate = 0.5
    item_test.apply_discount()
    assert item_test.price == 5.1

def test_item_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv('tests/test_items.csv')
    assert len(Item.all) == 4
    assert Item.all[0].name == 'Осцилограф'
    assert Item.all[0].quantity == 0
    assert Item.all[2].quantity == 5
    assert Item.all[3].price == 50.5

def test_item__repr__(item_test):
    assert repr(item_test) == "Item('Миксер', 10.2, 15)"

def test_item__str__(item_test):
    assert str(item_test) == "Миксер"

def test_item_add (item_test, phone_test):
    assert item_test + phone_test == 20

def test_item_add_noclass(phone_test):
    '''
    проверка на сложение экземпляров вне класса
    '''
    try:
        phone_test + 10
    except Exception as e:
        assert e


