"""Тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, NotFoundCSVError, InstantiateCSVError
from src.keyboard import Keyboard
from src.phone import Phone


def test_item():
    """
    Тестирование создание экземпляра item
    """
    item = Item("Телевизор", 100_000, 3)
    assert item.name == "Телевизор"
    assert item.price == 100_000
    assert item.quantity == 3


def test__repr__():
    """
    Тестирование отладки
    """
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test__str__():
    """
    Тестирование выведения названия
    """
    item = Item("Телевизор", 100_000, 3)
    assert str(item) == "Телевизор"


def test_calculate_total_price():
    """
    Тестирование общей стоимости товара в магазине
    """
    item = Item("Телевизор", 100_000, 3)
    assert item.calculate_total_price() == 300_000


def test_apply_discount():
    """
    Проверка применения скидки
    """
    item = Item("Телевизор", 100_000, 3)
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 50_000


def test__add__():
    """
    Проверка сложения экземпляров
    """
    item1 = Item("Телевизор", 100_000, 6)
    phone1 = Phone("Sumsung", 100_000, 3, 1)
    assert item1 + phone1 == 9
    assert phone1 + phone1 == 6


def test_name():
    """
    Проверка на превышение 10 символов в name
    """
    item = Item('Телефон', 10000, 5)
    item.name = "СуперСмартфон"
    assert item.name == 'СуперСмарт'


def test_instantiate_from_csv():
    """
    Проверка инициализации экземпляра класса `Item`
    """
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    test_item = Item.all[2]
    assert test_item.price == 10
    assert test_item.name == "Кабель"

    with pytest.raises(NotFoundCSVError):
        Item.instantiate_from_csv('asdf.csv')

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('items_incorrect.csv')


def test_string_to_number():
    """
    Тестирование на возвращение числа из числа-строки
    """
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_number_of_sim():
    """
    Проверяем, чтобы кол-во сим-карт было целым, неотрицательным числом
    """
    phone3 = Phone("Супермегафон", 1000000, 2, 6)
    with pytest.raises(ValueError):
        phone3.number_of_sim = -1
