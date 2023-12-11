import pytest

from src.item import Item


# Создаем тестовый экземпляр товара для использования в тестах
@pytest.fixture
def test_item():
    return Item("Test Item", 10.0, 5)


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 50.0


def test_apply_discount(test_item):
    test_item.apply_discount()
    assert test_item.price == 10.0 * Item.pay_rate


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv('./src/items.csv')
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_str_and_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
