import pytest

from src.phone import Phone


def test_phone_initialization(phone):
    assert phone.name == "Test Phone"
    assert phone.price == 500
    assert phone.quantity == 10
    assert phone.number_of_sim == 2


def test_phone_repr(phone):
    expected_repr = "Phone('Test Phone', 500, 10, 2)"
    assert repr(phone) == expected_repr


def test_invalid_number_of_sim_setter(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = 0


def test_number_of_sim_setter(phone):
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1


def test_phone_addition(phone):
    other_phone = Phone("Other Phone", 300, 5, 1)
    total_quantity = phone + other_phone
    assert total_quantity == 15


def test_addition_other_is_not_instance(phone):
    total_quantity = phone + 10
    assert total_quantity is None
