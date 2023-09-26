"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src import item


def item_item():
    return item.Item("Смартфон", 10000, 20)


def test___init__():
    assert item_item().__init__("Смартфон", 10000, 20) is None


def test_calculate_total_price():
    assert item_item().calculate_total_price() == 200000


def test_apply_discount():
    assert item_item().apply_discount() is None


@property
def test_fullname():
    assert item_item().fullname('Смартфон') == 'Смартфон'
    assert item_item().fullname('Телевизор филипс') == 'Телевизор '
    assert len(item_item().all) == 5


def test_string_to_number():
    assert item_item().string_to_number('5') == 5
    assert item_item().string_to_number('5.0') == 5
    assert item_item().string_to_number('5.5') == 5


def test_instantiate_from_csv():
    item_item().instantiate_from_csv('items.csv')  # создание объектов из данных файла


if __name__ == '__main__':
    pytest.main()
