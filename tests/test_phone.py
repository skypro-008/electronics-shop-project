import pytest

from src.phone import Phone


@pytest.fixture()
def phone():
    phone = Phone("iPhone 15", 120_000, 5, 2)
    return phone


def test_phone_init(phone):
    assert phone.number_of_sim == 2


def test__repr__(phone):
    assert repr(phone) == "Phone('iPhone 15', 120000, 5, 2)"