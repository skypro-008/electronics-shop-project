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
    assert item
