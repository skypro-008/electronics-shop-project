from src.phone import Phone

import pytest


@pytest.fixture
def item():
    item = Phone(name="Мерседес", price=45.97, quantity=40, sim=5)
    return item
def test_str(item):
    assert str(item) == "Мерседес"

def test_repr(item):
    assert repr(item) == "Phone('Мерседес', 45.97, 40, 5)"

def test_value_sim(item):
    assert item.number_of_sim == 5
    item.number_of_sim = 6
    assert item.number_of_sim == 6

def test_number_of_sim():
    phone = Phone('Iphone 12', 12000, 35, 2)
    with pytest.raises(ValueError):
        phone.number_of_sim = 2.5

def test_number_of_sim2():
    phone = Phone('Iphone 12', 12000, 35, 0)
    with pytest.raises(ValueError):
        phone.number_of_sim = -2