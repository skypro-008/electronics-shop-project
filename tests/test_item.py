import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 150, 2)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 300


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 150.0


@pytest.fixture
def item_notebook():
    return Item("Ноутбук", 250, 2)


def test_calculate_total_price_notebook(item_notebook):
    assert item_notebook.calculate_total_price() == 500


def test_apply_discount_notebook(item_notebook):
    item_notebook.apply_discount()
    assert item_notebook.price == 250.0


def test_name_setter():
    item = Item('Компьютер', 100, 2)
    assert item.name == 'Компьютер'


def test_instantiate_from_csv():
    file_csv = "Смартфон,100,1\nНоутбук, 1000, 3\n"
    with open("test_items.csv", "w", encoding="utf-8") as f:
        f.write(file_csv)
