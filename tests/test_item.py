"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_calculate_total_price():
    prod1 = Item("Телевизор", 50, 5)

    assert Item.calculate_total_price(prod1) == 250


def test_apply_discount():
    prod1 = Item("Телевизор", 50, 5)
    pay_rate = 2

    assert Item.apply_discount(prod1) == None


def test_name():
    Item.name = 'Шкода'
    assert Item.name == 'Шкода'


@pytest.fixture
def item():
    Item.all = []
    item = Item(name="Мерседес-Бенз", price=45.97, quantity=40)
    return item



def test_all_items_list(item):
    assert len(Item.all) == 1
    assert Item.all[0] == item


def test_len_name(item):
    with pytest.raises(Exception) as e:
        item.name = "Мерседес-Бенз"
        assert str(e.value) == "Длина наименования товара превышает 10 символов"


def test_len_name2(item):
    item.name = "Шоколад"
    assert item.name == "Шоколад"


def test_instantiate_from_csv(item):
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert isinstance(Item.all[0], Item)

def test_instantiate_from_csv_invalid_file(capfd):
    Item.instantiate_from_csv("test.csv")
    captured = capfd.readouterr()
    assert f"_Отсутствует файл test.csv_" in captured.out

def test_instantiate_from_csv_invalid_error(capfd):
    Item.instantiate_from_csv("../tests/test2.csv")
    captured = capfd.readouterr()
    assert f"Файл ../tests/test2.csv поврежден" in captured.out


def test_repr(item):
    assert repr(item) == "Item('Мерседес-Бенз', 45.97, 40)"


def test_str(item):
    assert str(item) == "Мерседес-Бенз"

def test_add(item):
    phone = Phone("Хонда",50, 40, 1)
    assert item + phone == 80

def test_not_add(item):
    with pytest.raises(ValueError) as y:
        item + 10
        assert str(y.value) == "Нельзя складывать"

