import pytest
from src.item import Item



@pytest.fixture
def item1():
    return Item('Lenovo', 50000, 5)


def test_item_quantity(item1):
    assert item1.quantity == 5


def test_item_name(item1):
    assert item1.name == 'Lenovo'


def test_item_price(item1):
    assert item1.calculate_total_price() == 250000


def test_apply_discount(item1):
    assert item1.apply_discount() == 50000


def test_instantiate_from_csv():
    """Тестируем инициализацию списка элементов класса Item из файла src/items.csv"""
    Item.instantiate_from_csv()
    # Общее количество элементов в загруженном списке
    assert len(Item.all) == 5
    # Проверяем корректность загрузки первого элемента
    item_test = Item.all[0]
    assert item_test.name == 'Смартфон'
    # Проверяем корректность загрузки четвертого элемента
    item_test = Item.all[3]
    assert item_test.name == 'Мышка'
    assert item_test.price == 50


def test_string_to_number():
    """Тестируем статический метод, возвращающий число из числа-строки."""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

