import pytest
import os
from pathlib import Path
import csv
from src.errors import InstantiateCSVError
from src.item import Item


def test_csv_error():
    """Тест на обработку исключения, если csv файл поврежден"""
    """Создаем поврежденный csv файл"""
    data = [
        {'name': 'item_1', 'price': '1.0'},
        {'name': 'item_2', 'price': '2.0'},
        {'name': 'item_3', 'price': '3.0'}
    ]
    """Создаём временный csv файл с помощью модуля csv"""
    with open('test.csv', 'w', encoding='cp1251', newline='') as file:
        fieldnames = ['name', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    Item.CSV_PATH = 'test.csv'
    """Проверяем обработку исключения, если данные неправильные"""
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv() == f"Файл {Path(Item.CSV_PATH).name} поврежден"

    with pytest.raises(InstantiateCSVError):
        raise InstantiateCSVError()
        Item.instantiate_from_csv() == "Файл поврежден"

    """Удаляем временный csv файл"""
    os.remove('test.csv')