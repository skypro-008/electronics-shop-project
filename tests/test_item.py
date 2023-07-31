import pytest
from src import item
from src import phone


def test_constructor():
    test_item = item.Item("Телевизор", 40000, 5)
    assert test_item.name == "Телевизор"
    assert test_item.price == 40000
    assert test_item.quantity == 5


def test_total_price():
    test_item1 = item.Item("Робот - пылесос", 23000, 10)
    test_item2 = item.Item("Планшет", 16000, 8)
    assert test_item1.calculate_total_price() == 230000
    assert test_item2.calculate_total_price() == 128000


def test_discount():
    test_item1 = item.Item("Смартфон", 15000, 5)
    test_item2 = item.Item("Фен", 6000, 15)

    item.Item.pay_rate = 0.8
    test_item1.apply_discount()
    test_item2.apply_discount()

    assert test_item1.price == 12000
    assert test_item2.price == 4800


def test_read_from_csv():
    item.Item.instantiate_from_csv()
    assert len(item.Item.all) == 5

    item_test = item.Item.all[2]
    assert item_test.name == "Кабель"

    for product in item.Item.all:
        assert isinstance(product, item.Item)


def test_string_to_number():
    assert item.Item.string_to_number('7') == 7
    assert item.Item.string_to_number('7.0') == 7
    assert item.Item.string_to_number('7.5') == 7

    with pytest.raises(ValueError):
        item.Item.string_to_number("hello")


def test_repr():
    test_item1 = item.Item("Робот - пылесос", 23000, 10)
    test_item2 = item.Item("Планшет", 16000, 8)

    assert repr(test_item1) == "Item('Робот - пылесос', 23000, 10)"
    assert repr(test_item2) == "Item('Планшет', 16000, 8)"


def test_str():
    test_item1 = item.Item("Смартфон", 15000, 5)
    test_item2 = item.Item("Фен", 6000, 15)

    assert str(test_item1) == 'Смартфон'
    assert str(test_item2) == 'Фен'


def test_add():
    phone1 = phone.Phone("iPhone 14", 150000, 5, 2)
    phone2 = phone.Phone("Xiomi Redme 9 Note", 15000, 10, 2)
    item1 = item.Item("Робот - пылесос", 23000, 10)
    item2 = item.Item("Планшет", 16000, 8)

    assert phone1 + phone2 == 15
    assert phone1 + item2 == 13
    assert item1 + item2 == 18
