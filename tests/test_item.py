"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_item():
    # классы для проверки
    item1 = Item('Car', 250.0, 8)
    item2 = Item('Ball', 130.0, 3)

    # Проверка общей цены
    assert item1.calculate_total_price() == 2000.0
    assert item2.calculate_total_price() == 390.0

    # Проверка скидки
    item1.pay_rate = 10.0
    item1.apply_discount()
    assert item1.price == 2500.0

    item2.pay_rate = 20.0
    item2.apply_discount()
    assert item2.price == 2600.0

    # Проверка списка экзепляров
    assert Item.all == [item1, item2]

def test_instantiate_from_csv():

    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.

    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5