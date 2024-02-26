import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1


def test___init__(phone):
    assert phone.name == "iPhone 14"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_repr():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert repr(phone1) == "Phone ('iPhone 14', 120000, 5, 2)"


def test_str():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert str(phone1) == 'iPhone 14'


@pytest.fixture
def testing_data():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1


def test_number_of_sim(testing_data):
    with pytest.raises(ValueError):
        testing_data.number_of_sim = -1
        testing_data.number_of_sim = 0
        testing_data.number_of_sim = 1.2
