import pytest
from src.item import Item

item1 = Item('Смартфон', 10, 5)


def test_item_init():
    assert item1.name == 'Смартфон'
    assert item1.price == 10
    assert item1.quantity != 10


def test_name_exception():
    item1.name = "Суперсмартфон"
    assert item1.name == "Смартфон"

    item1.name = 'Смарт'
    assert item1.name == 'Смарт'


def test_apply_discount():
    Item.pay_rate = 0.9
    assert item1.pay_rate == 0.9
    item1.apply_discount()
    assert item1.price == 9


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 7


#     poetry run pytest --cov