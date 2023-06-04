"""Тесты для модуля Item"""
import pytest

from src.item import Item

from src.phone import Phone

@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)

@pytest.fixture()
def make_item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture()
def make_phone():
    return Phone("iPhone 14", 120000, 5, 2)



def test_init(item):
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20


"""Выводим стоимость товара"""
def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


"""Устанавливаем скидку на товары"""


def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0
    assert item.calculate_total_price() == 160000.0


def test_instantiate_from_csv() -> None:
    Item.all.clear()
    Item.instantiate_from_csv('..\src\items.csv')
    assert len(Item.all) == 5
    assert Item.instantiate_from_csv('no_file') == 'Файл не найден'


def test_string_to_number():
    assert Item.string_to_number('5') == 5


def test__repr__():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', '10000.0', '20')"


def test__str__():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_name(item):
    item.name = 'Айфон'
    assert item.name == "Айфон"
    with pytest.raises(Exception):
        item.name = 'СуперПуперАйфон'



def test_addition(make_item, make_phone):
    item1 = make_item
    phone1 = make_phone
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(ValueError):
        assert item1 + 10 == 40
        assert phone1 + 5 == 20



    



