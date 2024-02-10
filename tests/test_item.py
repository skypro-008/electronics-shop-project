from src.item import Item
import pytest

@pytest.fixture
def item1():
    item1 = Item("Часы", 16000, 30)
    item = Item('Телефон', 55000, 10)
    return item1

@pytest.fixture
def item2():
    item2 = Item('Телефон', 55000, 10)
    return item2


def test_init(item1):
    assert item1.price == 16000
    assert item1.quantity == 30


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 480000


def instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

def test_name_setter_truncate(item2):
    item2.name = 'Телефонсмарт'
    assert item2.name == 'Телефонсма'

def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('10.0') == 10
    assert Item.string_to_number('17.5') == 17


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'
