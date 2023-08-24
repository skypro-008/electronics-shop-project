import pytest
from src.item import Item


@pytest.fixture()
def item_instance_kept():
    yield Item("", 0, 0)
    Item.all.clear()


@pytest.fixture()
def safe_item_class():
    Item.keep = False
    yield Item
    Item.keep = True


@pytest.mark.parametrize("price, discount, expected_result", [
    (12, 0.5, 6),
    (18, 1, 18),
])
def test_Item_apply_discount(safe_item_class, price, discount, expected_result):
    test_item_1 = safe_item_class("", price, 0)
    test_item_1.pay_rate = discount
    test_item_1.apply_discount()

    assert test_item_1.price == expected_result


@pytest.mark.parametrize("price, quantity, expected_result", [
    (5, 7, 35),
    (2.5, 3, 7.5)
])
def test_Item_calculate_total_price(safe_item_class, price, quantity, expected_result):
    test_item_1 = safe_item_class("", price, quantity)

    assert test_item_1.calculate_total_price() == expected_result


def test_Item_all(item_instance_kept):
    assert Item.all[0] is item_instance_kept
