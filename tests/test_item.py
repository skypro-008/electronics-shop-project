import os

import pytest

from src.item import Item
from src.phone import Phone

# Получение пути к текущему исполняемому файлу
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = current_dir[: -(len(current_dir.split("\\")[-1]) + 1)]

# Создание относительного пути к файлу от текущего файла
file_path = os.path.join(base_dir, "src", "items.csv")


@pytest.fixture
def data_item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def data_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_instantiate_from_csv():
    Item.instantiate_from_csv(file_path)  # создание объектов из данных файла
    assert len(Item.all) == 5


@pytest.mark.parametrize(
    "nm, pr, qt, disc", [("TV", 50_000, 10, 0.8), ("Tablet", 1500, 20, 1.2), ("Calculator", 500, 150, 0.9)]
)
def test_item(nm, pr, qt, disc):
    item = Item(nm, pr, qt)
    assert item.get_name == nm
    assert item.price == pr
    assert item.quantity == qt
    assert item.calculate_total_price() == pr * qt
    Item.pay_rate = disc
    item.apply_discount()
    assert item.price == pr * disc


@pytest.mark.parametrize("name, cls_name", [("Телефон", "Телефон"), ("СуперСмартфон", "СуперСмарт")])
def test_get_name(name, cls_name):
    new_item = Item.all[0]
    new_item.get_name = name
    assert new_item.get_name == cls_name


@pytest.mark.parametrize("num, res", [("10", 10), ("6.0", 6), ("7.7", 7)])
def test_string_to_number(num, res):
    assert Item.string_to_number(num) == res


def test_repr_str_item(data_item):
    item1 = data_item
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == "Смартфон"


def test__add__(data_item, data_phone):
    item1 = data_item
    item2 = data_item
    phone = data_phone

    assert item1 + item2 == 40
    assert item1 + phone == 25
    assert phone + item2 == 25


def test_raise_add__(data_item):
    with pytest.raises(ValueError, match="Эти данные нельзя сложить."):
        data_item + 20
