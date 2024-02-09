"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
import os


data = Item("Смартфон", 10000, 20)

def test_calculate_total_price():
    """проверяет правильность метода, который рассчитывает общую стоимость конкретного товара в магазине"""
    assert data.calculate_total_price() == 200000
    assert data.quantity ==20


def test_apply_discount():
    """Проверяет правильность метода, который применяет установленную скидку для конкретного товара"""
    data.pay_rate = 0.8
    data.apply_discount()
    assert data.price == 8000


def test_name_setter():
    """ проверяет длину наименования товара"""

    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name1 = 'СуперСмартфон'
    assert item.name1 == 'СуперСмартфон'


def test_instantiate_from_csv():
    Item.instantiate_from_csv(os.path.join('src', 'items.csv'))
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


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



