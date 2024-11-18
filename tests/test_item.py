"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import csv
import os
from src.item import Item, InstantiateCSVError
from src.phone import Phone

@pytest.fixture
def test_item_initialization():
    item = Item('Test Item', 100.0, 5)
    assert item.name == "Test Item"
    assert item.price == 100.0
    assert item.quantity == 5

def test_calculate_total_price():
    item = Item("Test Item", 100.0, 5)
    assert item.calculate_total_price() == 500.0

def test_apply_discount():
    item = Item("Test Item", 100.0, 5)
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 80.0

def test_apply_discount_with_default_rate():
    item = Item("Test Item", 100.0, 5)
    item.apply_discount()
    assert item.price == 100.0


def test_name_setter():
    item = Item('Test Item', 100.0, 5)

    item.name = "Short"
    assert item.name == "Short"

    # Проверка обрезки длинного имени
    long_name = "This is a very long name"
    item.name = long_name
    assert item.name == long_name[:10]

@pytest.mark.parametrize("s, expected", [
    ("10", 10),
    ("15.5", 15),
    ("20.9", 20),
    ("5.7", 5),
    ("100.0", 100),
])
def test_string_to_number(s, expected):
    assert Item.string_to_number(s) == expected


@pytest.fixture
def setup_test_csv(tmp_path):
    # Создание временного CSV-файла для тестирования
    file_path = tmp_path / "test_items.csv"
    with open(file_path, 'w', newline='', encoding='cp1251') as csvfile:
        fieldnames = ["name", "price", "quantity"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"name": "Тестовый товар 1", "price": "50.0", "quantity": "10"})
        writer.writerow({"name": "Тестовый товар 2", "price": "75.5", "quantity": "5"})
    return file_path


def test_instantiate_from_csv(setup_test_csv):
    file_path = setup_test_csv
    Item.instantiate_from_csv(file_path)

    assert len(Item.all) == 2

    item1 = Item.all[0]
    assert item1.name == "Тестовый товар 1"
    assert item1.price == 50.0
    assert item1.quantity == 10

    item2 = Item.all[1]
    assert item2.name == "Тестовый товар 2"
    assert item2.price == 75.5
    assert item2.quantity == 5

def test_repr_from_item():
    item1 = Item("somthing", 22000, 9)
    item2 = Item("Алибаба", 4, 13)

    assert repr(item1) == "Item('somthing', 22000, 9)"
    assert repr(item2) == "Item('Алибаба', 4, 13)"

def test_str_from_item():
    item1 = Item("somthing", 22000, 9)
    item2 = Item("Алибаба", 4, 13)

    assert str(item1) == 'somthing'
    assert str(item2) == 'Алибаба'

def test_add_from_item():
    item1 = Item('Iphone', 1200, 3)
    phone1 = Phone('Bebe', 12030, 1, 2)

    assert item1 + phone1 == 4

@pytest.fixture
def csv_file_path(tmpdir):
    file = tmpdir.join("src.item.csv")
    return str(file)

# Тест для проверки, что выбрасывается исключение FileNotFoundError
def test_file_not_found(csv_file_path):
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(file_path="non_existent_file.csv")

# Тест для проверки, что выбрасывается исключение InstantiateCSVError
def test_incomplete_csv_file(csv_file_path):
    with open(csv_file_path, 'w', encoding='cp1251') as file:
        file.write("name,price\n")  # Поврежденный файл без колонки quantity

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(file_path=csv_file_path)

# Тест для проверки корректной работы метода instantiate_from_csv
def test_valid_csv_file(csv_file_path):
    with open(csv_file_path, 'w', encoding='cp1251') as file:
        file.write("name,price,quantity\n")
        file.write("item1,100.0,10\n")
        file.write("item2,200.5,20\n")

    Item.instantiate_from_csv(file_path=csv_file_path)

    assert len(Item.all) == 2
    assert Item.all[0].name == "item1"
    assert Item.all[0].price == 100.0
    assert Item.all[0].quantity == 10
    assert Item.all[1].name == "item2"
    assert Item.all[1].price == 200.5
    assert Item.all[1].quantity == 20



