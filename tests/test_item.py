import pytest
from src.item import Item


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


@pytest.mark.parametrize('file_name, expected_result', [
    ('src/items.csv', 5)
])
def test_Item_instantiate_from_csv(file_name, expected_result):
    try:
        Item.instantiate_from_csv(file_name)

        assert len(Item.all) == expected_result

    finally:
        Item.all.clear()


@pytest.mark.parametrize('name, expected_result', [
    ('Name1', 'Name1')
])
def test_Item_name_prop(safe_item_class, name, expected_result):
    item1 = safe_item_class('', 0, 0)

    item1.name = name
    assert item1.name == expected_result


@pytest.mark.parametrize('name, max_len', [
    ('1234', 3),
    ('123', 2),
])
def test_Item_name_prop_max_len(safe_item_class, name, max_len):
    item1 = safe_item_class('', 0, 0)

    safe_item_class.max_name_len = max_len

    with pytest.raises(Exception) as ex:
        item1.name = name


@pytest.mark.parametrize('str_in, expected_result', [
    ('12', 12),
    ('12.0', 12),
    ('12.6', 12)
])
def test_Item_str_to_num(str_in, expected_result):
    assert Item.string_to_number(str_in) == expected_result


def test_Item_repr(safe_item_class):
    item1 = safe_item_class("Name", 1, 2)
    assert repr(item1) == "Item('Name', 1, 2)"


def test_Item_str(safe_item_class):
    item1 = safe_item_class("Name", 0, 0)
    assert str(item1) == "Name"


def test_Item_add(safe_item_class):
    item1 = safe_item_class("", 0, 5)
    item2 = safe_item_class("", 0, 10)

    assert item1 + item2 == 15


def test_Item_add_raise_TypeError(safe_item_class):
    item1 = safe_item_class("", 0, 5)
    item2 = 10

    with pytest.raises(TypeError):
        _ = item1 + item2
