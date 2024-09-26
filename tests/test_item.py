import os
from pathlib import Path
import csv
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def fix_item_class():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def fix_phone_class():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_calculate_total_price(fix_item_class):
    """Общая стоимость товара = кол-во * на стоимость"""
    assert fix_item_class.calculate_total_price() == 200000


def test_apply_discount(fix_item_class):
    """При применении скидки цена товара становится меньше"""
    fix_item_class.pay_rate = 0.7
    fix_item_class.apply_discount()
    assert fix_item_class.price == 7000.0


def test_all(fix_item_class):
    """Аргумент self.all добавляет экземпляры класса в список при инициализации"""
    assert type(fix_item_class.all) is list
    assert bool(fix_item_class.all) is True


def test_instantiate_from_csv():
    """С помощью временно csv файла
    проверяем корректность получения данных и обработки ошибок"""
    data = [
        {'name': 'item_1', 'price': '1.0', 'quantity': '1'},
        {'name': 'item_2', 'price': '2.0', 'quantity': '2'},
        {'name': 'item_3', 'price': '3.0', 'quantity': '3'}
    ]

    """Создаём временный csv файл с помощью модуля csv"""
    with open('test.csv', 'w', encoding='cp1251', newline='') as file:
        fieldnames = ['name', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    """Создание объектов из данных временного файла csv"""
    Item.CSV_PATH = 'test.csv'
    Item.all = []
    Item.instantiate_from_csv()

    """Проверка данных на корректность записи"""
    assert len(Item.all) == 3
    assert Item.all[1].name == 'item_2'
    assert Item.all[0].price == 1.0
    assert Item.all[2].quantity == 3

    """Удаляем временный csv файл"""
    os.remove('test.csv')

    """Проверяем отработку исключений, если файл не существует"""
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv() == f"Отсутствует файл {Path(Item.CSV_PATH).name}"


def test_string_to_number():
    """Возвращает число из числа-строки"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name(fix_item_class):
    """Перезаписывает приватный атрибут name, сокращает строку до 10 символов"""
    item = fix_item_class
    item.name = 'Телефон'
    assert item.name == 'Телефон'
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'


def test_repr(fix_item_class):
    """Возвращает строковое представление экземпляра класса"""
    assert repr(fix_item_class) == f"Item('{fix_item_class.name}', {fix_item_class.price}, {fix_item_class.quantity})"


def test_str(fix_item_class):
    """Возвращает строковое представление экземпляра класса"""
    assert str(fix_item_class) == fix_item_class.name


def test_add(fix_item_class, fix_phone_class):
    """Тест сложения родственных классов"""
    assert fix_item_class + fix_phone_class == 25
    assert fix_phone_class + fix_phone_class == 10
    with pytest.raises(ValueError):
        assert fix_phone_class + 5 == 'Складывать можно только объекты Item и дочерние от них.'
        assert fix_item_class + 5 == 'Складывать можно только объекты Item и дочерние от них.'
