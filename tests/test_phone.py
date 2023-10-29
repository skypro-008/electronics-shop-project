import pytest
from src.item import Item
from src.phone import Phone


phone1 = Phone("iPhone 14", 120_000, 5, 2)


item1 = Item("Смартфон", 10000, 20)
assert item1 + phone1 == 25
assert phone1 + phone1 == 10


def test_phone_number_of_sim_validation():
    with pytest.raises(ValueError):
        phone1 = Phone("iPhone 14", 120_000, 5, 0)  # Попытка создать объект с недопустимым значением для number_of_sim


def test_phone_repr():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_str():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone) == "iPhone 14"


def test_add_phone_and_item():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert phone1 + item1 == 25

def test_add_phone_and_phone():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    phone2 = Phone("Samsung Galaxy", 100000, 5, 1)
    assert phone1 + phone2 == 10
