"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from config import ITEMS

@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)

def test_item(item):
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20

def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000

def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0

def test_name(item):
    """Тест проверки длины наименования товара(не больше 10 символов)"""
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    item1.name = "Вечерняя поверка"
    assert item1.name == "Вечерняя п"


def test_instantiate_from_csv():
    """Проверка добавления экземпляров класса из CSV файла"""
    Item.instantiate_from_csv(ITEMS)
    assert len(Item.all) == 5


def test_string_to_number():
    """Проверка возвращения числа из строки-числа"""
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("3.5") == 3



