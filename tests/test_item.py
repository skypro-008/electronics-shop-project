from src.item import Item
import pytest


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    if Item.pay_rate == 0.8:
        assert item.apply_discount() == 8000.0


@pytest.fixture
def item_notebook():
    return Item("Ноутбук", 20000, 5)


def test_calculate_total_price_notebook(item_notebook):
    assert item_notebook.calculate_total_price() == 100000


def test_apply_discount_notebook(item_notebook):
    if Item.pay_rate == 0.8:
        assert item_notebook.apply_discount() == 20000
