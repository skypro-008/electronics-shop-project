import pytest
from src.phone import Phone

@pytest.fixture()
def make_phone():
    return Phone("iPhone 14", 120000, 5, 2)


def test_repr(make_phone):
    phone1 = make_phone
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(make_phone):
    phone1 = make_phone
    assert str(phone1) == 'iPhone 14'


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2


def test_number_of_sim_wrong(make_phone):
    phone1 = make_phone
    with pytest.raises(ValueError):
        phone1.number_of_sim = -1

