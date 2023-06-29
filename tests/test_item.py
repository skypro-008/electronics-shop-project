import pytest
from src.item import Item


@pytest.fixture
def cls_item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def cls_item_2():
    item = Item('Телефон', 10000, 5)
    item.name = 'СуперСмартфон'
    return item.name


def test_calculate_total_price(cls_item):
    assert cls_item.calculate_total_price() == cls_item.quantity*cls_item.price
    assert cls_item.calculate_total_price() == 200000


def test_apply_discount(cls_item):
    assert cls_item.price == 10000
    Item.pay_rate = 0.8
    cls_item.apply_discount()
    assert 8000.0 == cls_item.price


def test_name(cls_item_2):
    assert cls_item_2 == 'СуперСмарт'


def test_string_to_number(cls_item):
    assert cls_item.string_to_number('5') == 5
    assert cls_item.string_to_number('5.0') == 5
    assert cls_item.string_to_number('5.5') == 5
