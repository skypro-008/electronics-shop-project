"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_init_item(item):
    assert item.name == "Смартфон"
    assert item.price == 10000.0
    assert item.quantity == 20
    assert Item.all == [item]


def test_calculate_total_price(item):
    assert isinstance(item.calculate_total_price(), float)
    assert item.calculate_total_price() == 200000.0


def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0
    assert isinstance(item.price, float)


def test_instantiate_from_csv(item):
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number(item):
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
