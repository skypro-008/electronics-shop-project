"""Здесь надо написать тесты с использованием pytest для модуля item."""
import errno

from src.item import Item, InstantiateCSVError
import os
import pytest
from csv import DictReader


def test_calculate_total_price():
    item = Item("Product", 10, 5)
    assert item.calculate_total_price() == 50


def test_apply_discount():
    item = Item("Product", 10, 5)
    Item.pay_rate = 0.8  # set the discount to 20%
    item.apply_discount()
    assert item.price == 8


def test_all_instances():
    Item.all.clear()
    item1 = Item("Product1", 10, 5)
    item2 = Item("Product2", 20, 3)
    assert Item.all == [item1, item2]


def test_item_repr():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item('Ноутбук', 20000, 5)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Ноутбук', 20000, 5)"


def test_item_str():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item('Ноутбук', 20000, 5)
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Ноутбук'


@pytest.fixture(scope="module")
def csv_data():
    filedir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(f'{filedir}/../src', 'items.csv'), 'r+', encoding='windows-1251') as csv_file:
        csv_reader = DictReader(csv_file)
        return [item for item in csv_reader]


def test_load_csv(csv_data):
    assert len(csv_data) > 0


def test_instantiate_from_csv(csv_data):
    Item.instantiate_from_csv()
    assert len(Item.all) == len(csv_data)


def test_instantiate_from_csv_success(tmp_path):
    # Создаем временный файл CSV с данными
    csv_data = "name,price,quantity\nProduct 1,10,5\nProduct 2,20,3\n"
    csv_file = tmp_path / "item.csv"
    csv_file.write_text(csv_data)

    # Вызываем метод instantiate_from_csv
    Item.instantiate_from_csv()

    # Проверяем, что список all был заполнен корректно
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[0].price == 100
    assert Item.all[0].quantity == 1
    assert Item.all[1].name == "Ноутбук"
    assert Item.all[1].price == 1000
    assert Item.all[1].quantity == 3


@pytest.fixture
def item3():

    return Item("телефон", 1, 1)


def test_file_not_found_exception(item3, monkeypatch):
    filename = "no_file.txt"

    def mock_open(*args, **kwargs):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)

    monkeypatch.setattr("builtins.open", mock_open)

    with pytest.raises(FileNotFoundError) as exception:
        item3.load_csv()

    assert str(exception.value) == f"[Errno 2] No such file or directory: '{filename}'"

def test_string_to_number():
    assert Item.string_to_number('15') == 15
    assert Item.string_to_number('15.5') == 15
    assert Item.string_to_number('17.0') == 17

def test_get_name():
    item = Item("Товар", 100, 5)
    assert item.get_name() == "Товар"