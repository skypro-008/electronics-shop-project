import pytest

from src.phone import Phone

def test_init(some_phone):
    assert some_phone.name == "iPhone 14"
    assert some_phone.price == 120000
    assert some_phone.quantity == 5
    assert some_phone.number_of_sim == 2

def test_number_of_sim(some_phone):
    assert some_phone.number_of_sim == 2
    some_phone.number_of_sim = 4
    assert some_phone.number_of_sim == 4
    with pytest.raises(ValueError):
        some_phone.number_of_sim = 0
        assert some_phone.number_of_sim == "Amount sim not > 0"

def test_repr_str(some_phone):
    assert str(some_phone) == 'iPhone 14'
    assert repr(some_phone) == "Phone('iPhone 14', 120000, 5, 2)"