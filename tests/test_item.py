"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def coll_test_item():
    test_item = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    return test_item


def test_create_class(coll_test_item):
    assert print(coll_test_item) == print('Item (name="Смартфон", price=1000.0, quantity=20)')


def test_all_class(coll_test_item):
    assert print(Item.all) == print([coll_test_item])


def test_calculate_total_price(coll_test_item):
    assert coll_test_item.calculate_total_price() == 200_000.0


def test_apply_discount(coll_test_item):
    coll_test_item.apply_discount()
    assert coll_test_item.price == 8000.0
