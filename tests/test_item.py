"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


item = Item("Смартфон", 1000, 2)


def test_calculate_total_price():
    assert item.calculate_total_price() == 2000


def test_apply_discount():
    assert item.apply_discount() is None

@property
def test_fullname():
    item1 = 'Смартфон'
    assert Item.fullname(item1) == 'Смартфон'
    item2 = 'ТелевизорФилипс'
    assert Item.fullname(item2) == "ТелевизорФи"


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv('items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5


def test_repr_str():
    item1 = Item("Смартфон", 1000, 2)
    assert repr(item1) == "Item('Смартфон', 1000, 2)"
    assert str(item1) == 'Смартфон'

def test_add_function():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert item + phone == 7
    assert phone + phone == 10
    assert item + 10 == 'Некорректная операция'
    assert phone + 10 == 'Некорректная операция'
    assert item + "10" == 'Некорректная операция'
    assert phone + "10" == 'Некорректная операция'


if __name__ == '__main__':
    pytest.main()
