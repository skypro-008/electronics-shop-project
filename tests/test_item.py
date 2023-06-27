import pytest
from src.item import Item


@pytest.fixture
def cls_item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(cls_item):
    assert cls_item.calculate_total_price() == cls_item.quantity*cls_item.price
    assert cls_item.calculate_total_price() == 200000


def test_apply_discount(cls_item):
    assert cls_item.apply_discount() == cls_item.price * Item.pay_rate
    assert cls_item.apply_discount() == 10000.0