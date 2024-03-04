import pytest
from src.item import Item
import os
"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture
def test_position():
    return Item('Smartphone', 550.00, 10)


def test_calculate_total_price(test_position):
    assert test_position.calculate_total_price() == 5500


def test_apply_discount(test_position):
    Item.pay_rate = 0.8
    test_position.apply_discount(Item.pay_rate)
    print(test_position)
    assert test_position.price == 440

def test_init_item(test_position):
    assert test_position.name == 'Smartphone'
    assert test_position.price == 550.00
    assert test_position.quantity == 10

def test_instantiate_from_csv():
    # Получаем текущую директорию, где находится файл test_item.py
    current_directory = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_directory, '..', 'src', 'items.csv')

    Item.instantiate_from_csv(csv_file_path)
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    #with pytest.raises(InstantiateCSVError):
        #assert Item.instantiate_from_csv('../src/incorrect.csv')




def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'