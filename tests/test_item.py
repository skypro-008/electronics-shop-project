"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import csv

from src.item import Item


@pytest.fixture
def item1():
    item1 = Item("Смартфон", 10000, 20)
    return item1


@pytest.fixture
def item2():
    item2 = Item("СуперСмартфон", 100000, 5)
    return item2


@pytest.fixture
def new_name():
    new_name = "СуперСмартфон"
    return new_name


@pytest.fixture
def value():
    value = '99.9'
    return value


@pytest.fixture
def row1():
    items_csv = '../src/items.csv'
    with open(items_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        list_row = [row for row in reader]
        row1 = list_row[0]
        return row1


def test__init__(item1):
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20
    assert len(Item.all) == 1


def test__repr__(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test__str__(item1):
    assert str(item1) == 'Смартфон'


def test__add__(item1, item2):
    assert item1.quantity + item2.quantity == 25


def test_calculate_total_price(item1):
    """
    При создании экземпляра класса со значениями name, price, quantity,
    функция calculate_total_price() вернет общую стоимость товара
    total_price = price * quantity
    """
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    """
    При создании экземпляра класса со значениями name, price, quantity,
    функция apply_discount() вернет цену товара (price) с применением
    уровня цен, заданного по умолчанию в классе (pay_rate = 1.0) или
    заданного после переопределения (pay_rate = 0.5)
    """
    item1.apply_discount()
    assert item1.price == 10000

    Item.pay_rate = 0.5
    item1.apply_discount()

    assert item1.price == 5000.0


def test_property_name(item2):
    """
    Геттер для `name` с использованием @property позволяет получить приватное значение
    'name' экземпляра
    """
    assert item2.name == "СуперСмартфон"


def test_name_setter(item2, new_name):
    """
    Cеттер `name` позволяет задать новое значение для 'name' экземпляра
    с учетом заданных условий для 'name': допускается наименование
    не больше 10 симвовов, в противном случае, строка обрезается
    (остаются первые 10 символов)
    """
    item2.name = new_name
    assert item2.name == "СуперСмарт"


def test_classmethod_instantiate_from_csv(row1):
    """
    Класс-метод instantiate_from_csv(), инициализирующий экземпляры
    класса `Item` данными из файла _src/items.csv. Считывает данные
    файла в вмде словаря с первой строкой row[0] с данными по ключам
    'name', 'price', 'quantity'
    """
    assert row1 == {'name': 'Смартфон', 'price': '100', 'quantity': '1'}
    name = Item.check_to_str(row1['name'])
    assert name == 'Смартфон'
    price = Item.check_to_float(row1['price'])
    assert price == 100.0
    quantity = Item.check_to_int(row1['quantity'])
    assert quantity == 1


def test_staticmethod_string_to_number(value):
    """Cтатический метод string_to_number() возвращает целое число из числа-строки"""
    assert Item.string_to_number(value) == 99


def test_staticmethod_check_to_str(value):
    """Cтатический метод check_to_str() возвращает тип str"""
    assert Item.check_to_str(value) == '99.9'


def test_staticmethod_check_to_float(value):
    """Cтатический метод check_to_float() возвращает тип float"""
    assert Item.check_to_float(value) == 99.9


def test_staticmethod_check_to_int(value):
    """Cтатический метод check_to_int(), возвращает тип int"""
    assert Item.check_to_int(value) == 99
