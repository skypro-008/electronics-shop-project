"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def item_fixture():
    fixture_object = Item("apple", 21.40, 400)
    return fixture_object


def test_info_in_obj():
    assert item_fixture().pay_rate == 1.0
    Item.pay_rate = 0.7
    assert item_fixture().pay_rate == 0.7

    assert type(item_fixture().name) == str
    assert type(item_fixture().price) == float
    assert type(item_fixture().quantity) == int

    # Тут мы проверяем правильность добавления экзэмпляра класса в список Item.all
    assert len(Item.all) == len(item_fixture().all) - 1


def test_calculate_total_price():
    assert item_fixture().price * item_fixture().quantity == item_fixture().calculate_total_price()


def test_apply_discount():
    price_fixture = Item("1", 1.0, 1)
    Item.pay_rate = 0.8
    price_fixture.apply_discount()
    assert price_fixture.price == 0.8
