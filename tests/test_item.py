"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import os
import pytest


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

    # Проверяем ДЗ 2

    # Создаем класс для проверки новых методов
    item6 = Item('Телефон', 10000, 5)

    # проверяем сеттер отправляя товар, у которого наименование более 10 символов
     #item6.name = 'СуперСмартфон'

    # Exception: Длина наименования товара превышает 10 символов.

    assert item6.name == 'Телефон'

    # проверяем сеттер товар, у которого наименование менее 10 символов
    item6.name = 'Смартфон'
    assert item6.name == 'Смартфон'
    with pytest.raises(Exception):
        item6.name = 'СуперСмартфон'

    # Запускаем метод вызывающий класс из файла
    Item.instantiate_from_csv()
    # Проверяем корректность работы метода, подсчетом записей
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item6 = Item.all[0]
    assert item6.name == 'Смартфон'
    # проверка стаческого метода, который возвращает число из числа-строки
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

    # Создаем экземпляр класса для проверки магических методов
    item = Item("Смартфон", 10000, 20)

    # Проверяем магический метод __repr__
    assert repr(item) == "Item('Смартфон', 10000, 20)"

    # Проверяем магический метод __str__
    assert str(item) == 'Смартфон'
