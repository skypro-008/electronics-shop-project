"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
from pathlib import Path
import pytest
import os
from src.item import Item

def test_init(some_item):
    assert some_item.name == "Смартфон"
    assert some_item.price == 10000
    assert some_item.quantity == 5

def test_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 50000


def test_apply_discount(some_item):
    some_item.pay_rate = 0.5
    some_item.apply_discount()
    assert some_item.price == 5000

def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

def test_instantiate_from_csv():
    """C помощью временного csv файла проверяем корректность получения данных и обработки ошибок"""
    data = [
        {'name': 'item_1', 'price': '1.0', 'quantity': '1'},
        {'name': 'item_2', 'price': '2.0', 'quantity': '2'},
        {'name': 'item_3', 'price': '3.0', 'quantity': '3'}
    ]

    # создаём временный csv файл с помощью модуля csv
    with open('test.csv', 'w', encoding='windows-1251', newline='') as file:
        fieldnames = ['name', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    # создание объектов из данных временного файла csv
    Item.CSV_PATH = 'test.csv'
    Item.all = []
    Item.instantiate_from_csv()

    # проверка данных на корректность записи
    assert len(Item.all) == 3
    assert Item.all[1].name == 'item_2'
    assert Item.all[0].price == 1.0
    assert Item.all[2].quantity == 3

    # удаляем временный csv файл
    os.remove('test.csv')

    # проверяем отработку исключений, если файл не существует
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv() == f"Отсутствует файл {Path(Item.CSV_PATH).name}"

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_name(some_item):
    some_item.name = 'Смартфон'
    assert some_item.name == 'Смартфон'
    some_item.name = 'СуперСмартфон'
    assert some_item.name == 'СуперСмарт'

def test_repr(some_item):
    assert repr(some_item) == "Item('Смартфон', 10000, 5)"

def test_str(some_item):
    assert str(some_item) == 'Смартфон'

def test_add(some_item, some_phone):
    assert some_item + some_phone == 10
    assert some_phone + some_phone == 10
    with pytest.raises(ValueError):
        assert some_item + 5 == 'Проверка, что можно сложить `Phone` или `Item` только с экземплярами `Phone` или `Item` классов.'
        assert some_phone + 5 == 'Проверка, что можно сложить `Phone` или `Item` только с экземплярами `Phone` или `Item` классов.'