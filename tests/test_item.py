import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def cls_item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def cls_item_2():
    item = Item('Телефон', 10000, 5)
    item.name = 'СуперСмартфон'
    return item.name


@pytest.fixture
def cls_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr(cls_item):
    assert repr(cls_item) == "Item('Смартфон', 10000, 20)"
    assert repr(cls_item) == f"{cls_item.__class__.__name__}('{cls_item.name}', {cls_item.price}, {cls_item.quantity})"


def test_str(cls_item):
    assert str(cls_item) == 'Смартфон'
    assert str(cls_item) == f"{cls_item.name}"


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


def test_add(cls_phone, cls_item):

    assert cls_phone + cls_item == 25
    assert cls_item + cls_phone == 25
    assert cls_item + cls_item == 40
    assert cls_phone + cls_phone == 10
    assert cls_phone + cls_item == cls_phone.quantity + cls_item.quantity
    assert cls_phone + cls_phone == cls_phone.quantity + cls_phone.quantity
