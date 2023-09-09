import pytest
from src.phone import Phone
from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_magic_methods(phone):
    assert str(phone) == 'iPhone 14'
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add(phone):
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone == 25
    assert phone + phone == 10


def test_setter(phone):
    assert phone.number_of_sim == 2
    with pytest.raises(ValueError):
        phone.number_of_sim = 0