"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

data = Item("Смартфон", 10000, 20)


def test_calculate():
    """
    Тестируем рассчет общей стоимость конкретного товара в магазине.
    """
    assert data.calculate_total_price() == 200000


def test_apply_discount():
    """
    Проверяем действие установленной скидки для конкретного товара.
    """
    data.pay_rate = 0.7
    data.apply_discount()
    assert data.price == 7000


def test_name():
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

item = Item('Телефон', 10000, 5)
item.name = 'Смартфон'
item.name = 'СуперСмартфон'

def test_instantiate_from_csv():
    """
    Cоздание объектов из данных файла
    """
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5


def test_string_to_number():
    """
     Преобразование строки в число
    """
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

