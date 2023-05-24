"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest as pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("item1", 10.0, 5)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50.0


def test_apply_discount(item):
    item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 9.0


def test_instantiate_from_csv(item):
    item.instantiate_from_csv()

    assert len(item.all) == 7


def test_all_items():
    item1 = Item("item1", 10, 5)
    item2 = Item("item2", 20, 2)
    assert Item.all == [item1, item2]


def test_string_to_number(item):
    assert item.string_to_number("10000") == 10000
    assert item.string_to_number("3.024") == 3


def test_personal_name_setter(item):
    """Тестируем сеттер """
    item.name = "Сони"
    assert item.name == "Сони"
