import pytest
import os
from src.item import Item, InstantiateCSVError

data = Item("Смартфон", 10000, 20)


# Проверяем, что атрибуты класса Item были установлены правильно
@pytest.fixture
def item():
    return Item("Название товара", 1000, 5)


def test_init(item):
    assert item.name == "Название товара"
    assert item.price == 1000
    assert item.quantity == 5


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 5000


def test_discaunt_price(item):
    item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 500


def test_name(self):
    """Тест сеттера name"""
    # data.name = "Смартфон"
    assert data.name == 'Смартфон'


def test_name():
    """Тест сеттера сокращающего длину имени до 10(и) символов."""
    item = Item("Abrakadabra", 1000, 5)
    assert len(item.name) == 11


def test_instantiate_from_csv():
    """
    Проверка метода инициализируеющнго экземпляры класса Item данными из файла src/items.csv
    """
    Item.instantiate_from_csv('items.csv')
    assert len(Item.all) == 10


def test_instantiate_from_csv():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(path_to_csv=r"../src/item.csv")

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(path_to_csv=r"../src/items.csv")


def test__repr__():
    """
    Тест магического метода repr
    """
    data.name = 'Смартфон'
    assert repr(data) == "Item('Смартфон', 10000, 20)"


def test_add():
    item2 = Item("Название товара", 1000, 5)
    assert item2 + item2 == 10


def test__str__():
    data.name = "Смартфон"
    """
    Тест магического метода str
    """

    assert str(data) == 'Смартфон'
