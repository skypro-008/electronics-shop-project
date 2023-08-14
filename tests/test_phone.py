import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone() -> Phone:
    return Phone("Iphone 12", 1000, 2, 1)

def test_count_sim(phone) -> None:
    assert phone.count_sim == 1


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10