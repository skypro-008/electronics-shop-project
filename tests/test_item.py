import pytest
from src.item import Item


@pytest.fixture()
def total_1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(total_1):
    assert total_1.calculate_total_price() == 200000


def test_apply_discount(total_1):
    if Item.pay_rate == 0.8:
        total_1.price = total_1.price * total_1.pay_rate
        assert total_1.price == 8000.0


@pytest.fixture()
def total_2():
    return Item("Ноутбук", 20000, 5)


def test_calculate_total_2_price(total_2):
    assert total_2.calculate_total_price() == 100000


def test_apply_discount_total_2(total_2):
    if Item.pay_rate == 0.8:
        total_2.price = total_2.price * total_2.pay_rate
        assert total_2.price == 20000
