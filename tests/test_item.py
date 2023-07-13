"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

test_item1 = Item("Утюг", 2000, 15)
test_item2 = Item("TV", 40000, 5)


def test_calculate_total_price():
    assert test_item1.calculate_total_price() == 30000
    assert test_item2.calculate_total_price() == 200000


def test_apply_discount():
    Item.pay_rate = 0.5
    test_item1.apply_discount()
    assert test_item1.price == 1000
    test_item2.apply_discount()
    assert test_item2.price == 20000


def test_string_to_number():
    assert Item.string_to_number('3') == 3
    assert Item.string_to_number('8.0') == 8
    assert Item.string_to_number('2.5') == 2


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_name_setter():
    item = Item('Смартфон', 10000, 5)
    assert item.name == "Смартфон"
    item.name = 'Кондиционер'
    assert item.name == "Кондиционе"
