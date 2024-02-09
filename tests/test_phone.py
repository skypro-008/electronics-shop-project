from src.phone import Phone
from src.item import Item
import pytest

@pytest.fixture()
def phone_example():
    return Phone("iPhone 15", 140000, 10, 2)

def test_repr(phone_example):
    assert phone_example.__repr__() == "Phone('iPhone 15', 140000, 10, 2)"

def test_number_of_sim(phone_example):
    phone_example.number_of_sim = 3
    assert phone_example.number_of_sim == 3

def test_add(phone_example):
    assert phone_example.quantity + phone_example.quantity == 20
    item_example = Item("Наушники", 5000, 20)
    assert phone_example.quantity + item_example.quantity == 30