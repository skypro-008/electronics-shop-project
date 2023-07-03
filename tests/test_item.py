import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000.0
    assert item2.calculate_total_price() == 100000.0


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000


def test_name():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("СуперСмартфон", 10000, 20)
    assert item1.name == "Смартфон"
    assert item2.name == "СуперСмартфон"
    assert print(item2.name) == print("Наименования товара должно быть не больше 10 симвовов")


def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert len(items) == 5

    item1 = items[0]
    assert item1.name == 'Смартфон'
    assert item1.price == 100
    assert item1.quantity == 1


def test_string_to_number():
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_get_price():
    phone1 = Phone("Смартфон", 10000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert item1 + 50 == 'Не экземпляр класса Item'
    assert phone1 + 50 == 'Не экземпляр класса Item'


def test_read_file():
    assert str(Item.instantiate_from_csv()) == "[Item('Смартфон', 100, 1), Item('Ноутбук', 1000, 3), Item('Кабель', 10, 5), Item('Мышка', 50, 5), Item('Клавиатура', 75, 5)]"

    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('items_none.csv')

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('item.csv')
