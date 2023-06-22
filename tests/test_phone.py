import pytest

from src.item import Item
from src.phone import Phone


def test_add_phone_and_item():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    item = Item("Смартфон", 10_000, 20)
    assert phone + item == 25
    assert item + phone == 25


def test_add_phone_and_other_object():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    with pytest.raises(TypeError):
        phone + "тест"


def test_invalid_number_of_sim():
    with pytest.raises(ValueError):
        phone = Phone("iPhone 14", 120_000, 5, -1)
        phone.number_of_sim = -2
