import pytest
import os
from src.item import Item
from src.item import InstantiateCSVError

"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture
def test_item():
    return Item


@pytest.fixture
def test_item1():
    return Item("Товар1", 100, 2)


@pytest.fixture
def test_item2():
    return Item("Товар2", 50, 3)


@pytest.fixture
def test_item_1_file():
    return os.path.join("..", "tests", "test_items1.csv")


@pytest.fixture
def test_item_2_file():
    return os.path.join("..", "tests", "test_items2.csv")


@pytest.fixture
def test_item_3_file():
    return os.path.join("..", "tests", "test_items.csv")


def test_repr(test_item1):
    assert test_item1.__repr__() == "Item('Товар1', 100, 2)"


def test_str(test_item2):
    assert test_item2.__str__() == 'Товар2'


def test_instantiate_from_csv(test_item1):
    assert len(test_item1.all) == 5


def test_instantiate_from_csv1(test_item_1_file):
    with pytest.raises(InstantiateCSVError, match='Файл item.csv поврежден'):
        Item.instantiate_from_csv(test_item_1_file)


def test_instantiate_from_csv2(test_item_2_file):
    with pytest.raises(InstantiateCSVError, match='Файл item.csv поврежден'):
        Item.instantiate_from_csv(test_item_2_file)


def test_instantiate_from_csv3(test_item_3_file):
    with pytest.raises(FileNotFoundError, match='Отсутствует файл item.csv'):
        Item.instantiate_from_csv(test_item_3_file)


def test_calculate_total_price(test_item1):
    assert test_item1.calculate_total_price() == 200.0


def test_apply_discount(test_item1):
    Item.pay_rate = 0.8
    test_item1.apply_discount()
    assert test_item1.price == 80.0


def test_name(test_item1):
    test_item1.name = "Комп"
    assert test_item1.name == 'Комп'
    test_item1.name = "СуперКомпьютер"
    assert test_item1.name == 'СуперКомпь'


def test_string_to_number():
    assert Item.string_to_number('6.0') == 6
    assert Item.string_to_number('6') == 6


def test_add(test_item1, test_phone1):
    assert test_item1 + test_phone1 == 4


def test_add2(test_item1):
    with pytest.raises(ValueError):
        test_item1 + 1
