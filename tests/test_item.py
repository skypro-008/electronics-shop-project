"""Здесь надо написать тесты с использованием pytest для модуля item."""
import os

import pytest

from src.item import Item

from src.phone import Phone


def test_calculate_total_price():
    """
    Тест функции "calculate_total_price"
    На рассчёт общщей стоймости конкретного товара
    """
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000


def test_apply_discount():
    """
    Тест функции "apply_discount"
    на расссчёт стоимости на товар с учётом скидки
    """
    item = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    assert item.apply_discount() == 8000


@pytest.fixture
def test_item_csv():
    """
    Декоратор для объявления пути к файлу для тестов
    """
    return f'{os.getcwd()}\\tests\\test_items.csv'


def test_instantiate_from_csv(test_item_csv):
    """
    Тест класс-метода instantiate_from_csv для инициализации класса Item данными из файла
    """
    Item.instantiate_from_csv(file=test_item_csv)
    assert len(Item.all) == 5


def test_name():
    """
    Тест декоратора Property и сеттера, который не должен пропускать названия товаров длиннее 10 символов
    """
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    with pytest.raises(Exception):
        item.name = 'ПортативнаяЗарядка'


def test_string_to_number():
    """
    Тест статик-метода преобразующего поступающее число в формате Str/Float в формат Int
    """
    assert Item.string_to_number("5555") == 5555
    assert Item.string_to_number("2222.5") == 2222


def test_repr():
    item = Item('Ноутбук', 80000, 24)
    assert repr(item) == "Item('Ноутбук', 80000, 24)"


def test_str():
    item = Item('Ноутбук', 80000, 24)
    assert str(item) == 'Ноутбук'


def test_add():
    """
    Тест для add функции на сложение экземпляров класса Phone и Item по общему количеству товара в магазине
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(Exception):
        assert item1 + 1
    with pytest.raises(Exception):
        assert phone1 + 1
