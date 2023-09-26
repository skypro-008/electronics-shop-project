import pytest
from src.phone import Phone
from src.item import Item

@pytest.fixture
def phone_fixture() -> Phone:
    phone = Phone("Honor 10", 10000, 5, 2)
    Phone.all.append(phone)
    return Phone

def test___repr__():
    phone = Phone("Iphone X", 20000, 5, 3)
    assert phone.__repr__() == "Phone('Iphone X', 20000, 5, 3)"

def test___str__():
    phone = Phone("Iphone X", 20000, 5, 3)
    assert phone.__str__() == 'Iphone X'

def test_phone():
    phone = Phone("Honor 10", 10000, 5, 2)
    assert phone.name == 'Honor 10'
    assert phone.price == 10000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2

def test___add__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("Samsung Galaxy", 30000, 10, 3)
    item1 = Item("Смартфон", 10000, 20)
    assert phone1 + item1 == 25
    assert phone1 + phone2 == 15
    assert phone1 + phone1 == 10
