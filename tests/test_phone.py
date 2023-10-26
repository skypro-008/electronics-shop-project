import pytest

from src.phone import Phone


@pytest.fixture
def phone_fixture():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1


def test__str__(phone_fixture):
    phone1 = phone_fixture
    assert str(phone1) == 'iPhone 14'


def test__repr__(phone_fixture):
    phone1 = phone_fixture
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(phone_fixture):
    phone1 = phone_fixture
    assert phone1.number_of_sim == 2
