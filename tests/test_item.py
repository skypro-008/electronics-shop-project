"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone
from src.item import InstantiateCSVError
import pytest


@pytest.fixture()
def phone_test():
    return Item("Смартфон", 10000, 20)


@pytest.fixture()
def phone_test1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_calculate(phone_test):
    """
    Тестируем рассчет общей стоимость конкретного товара в магазине.
    """
    assert phone_test.calculate_total_price() == 200000


def test_apply_discount(phone_test):
    """
    Проверяем действие установленной скидки для конкретного товара.
    """
    phone_test.pay_rate = 0.7
    phone_test.apply_discount()
    assert phone_test.price == 7000


def test_name_setter(phone_test):
    item = phone_test
    item.name = "СуперCмартфон"
    assert item.name == 'СуперCмарт'


def test_instantiate_from_csv():
    """
    Cоздание объектов из данных файла
    """
    Item.instantiate_from_csv("../src/item.csv")
    assert len(Item.all) == 5


def test_instantiate_from_csv_not_file():
    """
    Отсутствие файла
    """
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("../src/item1.csv")


def test_instantiate_from_csv_bad_file():
    """
    Поврежденный файл
    """
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("../src/item2.csv")


def test_string_to_number():
    """
     Преобразование строки в число
    """
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(phone_test):
    """
    Тест магического метода __repr__

    """
    phone_test.price = phone_test.string_to_number(phone_test.price)
    assert repr(phone_test) == "Item('Смартфон', 10000, 20)"


def test_str(phone_test):
    """
    Тест магического метода  __str__.
    """
    assert str(phone_test) == 'Смартфон'


def test__add__(phone_test, phone_test1):
    assert phone_test + phone_test1 == 25
    assert phone_test1 + phone_test1 == 10
