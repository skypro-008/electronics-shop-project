import pytest
from src.phone import Phone


@pytest.fixture
def make_items():
    phone1 = Phone("iPhone", 100000, 20, 1)
    phone2 = Phone("Samsung", 20000, 5, 2)
    return phone1, phone2


def test_repr(make_items):
    phone1 = make_items[0]
    phone2 = make_items[1]
    assert repr(phone1) == "Phone('iPhone', 100000, 20, 1)"
    assert repr(phone2) == "Phone('Samsung', 20000, 5, 2)"
