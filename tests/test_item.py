import pytest

from src.item import Item


@pytest.fixture()
def expl1():
    return Item("Смартфон", 10000, 20)


def test_item_init(expl1):
    assert expl1.name == "Смартфон"
    assert expl1.price == 10000
    assert expl1.quantity == 20


def test_calculate_total_price(expl1):
    assert expl1.calculate_total_price() == 200000


def test_apply_discount(expl1):
    Item.apply_discount(expl1)
    assert expl1.price == 10000.0