"""Здесь надо написать тесты с использованием pytest для модуля item."""

from config import OPERATIONS_PATH
from src.item import Item


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    assert item1.price * Item.pay_rate == 8000.0
    assert item1.price * Item.pay_rate == 8000.0


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


@property
def test_name():
    item = Item("Смартфон", 10000, 20)
    assert item.name == 'Смартфон'
    item1 = Item("СуперСмартфон", 10000, 20)
    assert item1.name == 'СуперСмарт'


def test_all():
    Item.instantiate_from_csv(OPERATIONS_PATH)
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_repr():
    item1 = Item('Смартфон', 10000, 20)
    assert repr(item1) == Item('Смартфон', 10000, 20)


def test_str():
    item1 = Item('Смартфон', 10000, 20)
    assert str(item1) == 'Смартфон'
