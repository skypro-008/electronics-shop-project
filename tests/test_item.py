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
    item = Item(name="Товар",price=45.97, quantity=40)
    return item
def test_all_items_list(item):
    assert len(Item.all) == 1
    assert Item.all[0] ==item

# def test_len_name(item):
#     with pytest.raises(ValueError) as e:
#         item.name = "Мерседес-Бенз"
#     assert str(e.value) == "Длина наименования товара превышает 10 символов"

def test_instantiate_from_csv(item):
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert isinstance(Item.all[0], Item)


