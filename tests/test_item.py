"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


# @pytest.mark.parametrize('price, quantity, expected', [
#     (10000, 20, 200000),
#     (20000, 5, 100000)
# ])
# def test_calculate_total_price(item, price):
#     assert item.calculate_total_price() == 10000
#     assert item.calculate_total_price() == 20000
#
#
# def test_apply_discount():
#     assert Item.apply_discount() == 10000
#     assert Item.apply_discount() == 20000
#
#
# @pytest.fixture()
# def item():
#     return Item("Смартфон, 10000. 20")
#
#
# def test_name(item):
#     assert isinstance(item, Item)
#     assert item.name == 'Название товара не соответствует'
#
#
# def test_instantiate_from_csv():
#     assert len(Item.all) == 5
#
#
# @pytest.mark.parametrize('number ,expected', [
#     ('5', 5),
#     ('5.0', 5),
#     ('5.5', 5)
# ])
# def test_string_to_number(number, expected):
#     assert Item.string_to_number(number) == expected


def test_repr():
    item1 = Item('Смартфон', 10000, 20)
    assert repr(item1) == 'Item(Смартфон, 10000, 20)'


def test_str():
    item1 = Item('Смартфон', 10000, 20)
    assert str(item1) == 'Смартфон'
