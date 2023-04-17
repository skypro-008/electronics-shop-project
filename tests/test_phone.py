import pytest

from src.item import Item
from src.phone import Phone


class New:
    """Класс не связанный с Item, для теста add"""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.number_of_sim = number_of_sim


@pytest.fixture
def return_date():
    """Описание фикстуры для тестов"""
    return Phone("Смартфон", 10000, 20, 1)


def test_init(return_date):
    """Тест для init"""
    assert return_date.price == 10000
    assert return_date.name == 'Смартфон'
    assert return_date.quantity == 20
    assert return_date.number_of_sim == 1


def test_number_of_sim():
    """Тест переменой количества симок"""
    date = Phone("Смартфон", 10000, 20, 2)
    assert date.number_of_sim == 2
    with pytest.raises(ValueError):
        date.number_of_sim = 0


def test_repr(return_date):
    """Тест для метода repr"""
    assert repr(return_date) == "Phone('Смартфон', 10000, 20, 1)"


def test_add():
    """Тест для метода сложения количества товара двух экземпляров"""
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    phone2 = New("iPhone 14", 120000, 5, 2)
    assert phone1 + item1 == 25
    assert phone1 + phone1 == 10
    assert item1 + item1 == 40
    with pytest.raises(Exception):
        phone1 + phone2
