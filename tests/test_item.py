import pytest

from src.item import Item


def test_calculate_total_price():
    prod1 = Item("Телевизор", 50, 5)
    assert prod1.calculate_total_price() == 250


@pytest.fixture
def item():
    Item.all = []
    item = Item(name="Товар", price=45.97, quantity=40)
    return item


def test_all_items_list(item):
    assert len(Item.all) == 1
    assert Item.all[0] == item


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert isinstance(Item.all[0], Item)

    # Проверка значений объектов, созданных из CSV файла
    item1 = Item.all[0]
    assert item1.name == "Смартфон"
    assert item1.price == 100
    assert item1.quantity == 1


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_invalid_name_length():
    prod1 = Item("Товар", 50, 5)
    prod1.name = "Наименование, которое не должно пройти проверку"
    assert prod1.name == "Товар"
