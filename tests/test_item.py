"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    assert Item.calculate_total_price(item1) == 200000.0

def test_name_setter():
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item._name == 'Смартфон'

    # длина наименования товара равна 10 символов
    item.name = '0123456789'
    assert item._name == '0123456789'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    assert item._name != 'СуперСмартфон'


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[1].name == "Ноутбук"