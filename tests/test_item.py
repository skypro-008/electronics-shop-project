"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000

    item2 = Item("Ноутбук", 20000, 5)
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item1.apply_discount()
    assert item1.price == 8000.0

    item2 = Item("Ноутбук", 20000, 5)
    item2.apply_discount()
    assert item2.price == 20000


def test_apply_discount_with_zero_discount():
    item1 = Item("Смартфон", 10000, 20)
    item1.apply_discount(0)
    assert item1.price == 10000

    item2 = Item("Ноутбук", 20000, 5)
    item2.apply_discount(0)
    assert item2.price == 20000


def test_apply_discount_with_hundred_percent_discount():
    item1 = Item("Смартфон", 10000, 20)
    item1.apply_discount(100)
    assert item1.price == 0.0

    item2 = Item("Ноутбук", 20000, 5)
    item2.apply_discount(100)
    assert item2.price == 0.0

def test_name():
    item = Item("Apple", 1.0, 10)
    assert item.name == "Apple"


def test_set_name():
    item = Item("Apple", 1.0, 10)
    item.name = "Banana"
    assert item.name == "Banana"


def test_set_long_name():
    item = Item("Apple", 1.0, 10)
    item.name = "LongNameForItem"
    assert item.name == "LongNameFo"


def test_calculate_total_price():
    item = Item("Apple", 1.0, 10)
    assert item.calculate_total_price() == 10.0


def test_apply_discount():
    Item.pay_rate = 0.9
    item = Item("Apple", 1.0, 10)
    item.apply_discount()
    assert item.price == 0.9


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


if __name__ == '__main__':
    test_name()
    test_set_name()
    test_set_long_name()
    test_calculate_total_price()
    test_apply_discount()
    test_instantiate_from_csv()
