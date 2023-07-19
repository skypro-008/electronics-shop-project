"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_name():
    item1 = Item("Телефон", 10000, 20)
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'
    item1.name = "СуперСмартфон"
    assert item1.name == 'СуперСмарт'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item2 = Item("Смартфон", 15000, 10)
    assert repr(item2) == "Item('Смартфон', 15000, 10)"


def test_str():
    item3 = Item("Ноутбук", 45000, 8)
    assert str(item3) == "Ноутбук"
