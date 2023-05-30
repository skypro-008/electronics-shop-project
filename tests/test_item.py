"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import csv
from src.item import Item


@pytest.fixture
def item1_2():
    Item.pay_rate = 1.1
    return Item("Декстоп", 400000, 2), Item("Клавиатура", 5000, 5)


def test_calculate_total_price(item1_2):

    assert item1_2[0].calculate_total_price() == 800000
    assert item1_2[1].calculate_total_price() == 25000


def test_apply_discount(item1_2):
    item1_2[0].apply_discount()
    item1_2[1].apply_discount()
    assert int(item1_2[0].price) == 440000
    assert int(item1_2[1].price) == 5500


def test_names(item1_2):

    assert item1_2[0].name == "Декстоп"
    assert item1_2[1].name == "Клавиатура"


def test_string_to_number():
    assert Item.string_to_number("42") == 42
    assert Item.string_to_number("3.14") == 3
    assert Item.string_to_number("abc") is None


@pytest.fixture
def csv_data():
    # Чтение данных из csv-файла
    items = []
    with open("../src/items.csv", newline='', encoding="cp1251") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            price = float(row['price'])
            quantity = int(row['quantity'])
            items.append((name, price, quantity))
    return items


def test_instantiate_from_csv(csv_data):
    # Вызов метода instantiate_from_csv()
    items = Item.instantiate_from_csv()

    # Проверка количества экземпляров класса Item
    assert len(items) == len(csv_data)

    # Проверка соответствия данных
    for item, (name, price, quantity) in zip(items, csv_data):
        assert item.name == name
        assert item.price == price
