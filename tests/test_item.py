"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.mark.parametrize('initial_price, quantity, total_price', [
    (50_000, 3, 150_000),
    (70_000, 2, 140_000),
    (30_000, 1, 30_000)
])
def test_calculate_total_price(item, initial_price, quantity, total_price):
    item.price = initial_price
    item.quantity = quantity
    total_price = initial_price * quantity

    assert item.calculate_total_price() == total_price


@pytest.mark.parametrize('pay_rate, initial_price, expected_price', [
    (0.85, 80_000, 68_000),
    (0.95, 120_000, 114_000),
    (0.5, 30_000, 15_000)
])
def test_apply_discount(item, pay_rate, initial_price, expected_price):
    item.pay_rate = pay_rate
    item.price = initial_price
    item.apply_discount()

    assert item.price == expected_price


@pytest.mark.parametrize('name, result_name', [
    ('Laptop Top-Top', 'Laptop Top'),
    ('IPhone X-Men Pro', 'IPhone X-M'),
    ('Smart Lamp But Not You', 'Smart Lamp'),
    ('AppleWatchingYou', 'AppleWatch'),
    ('Lenovo 4Vova', 'Lenovo 4Vo'),
    ('This Is 10', 'This Is 10'),
    ('Only 1', 'Only 1')
])
def test_name(item: object, name: str, result_name: str):
    item.name = name

    assert item.name == result_name


@pytest.mark.parametrize('string_value, int_result', [
    ('3.5', 3),
    ('8.2', 8),
    ('4.0', 4),
    ('9', 9)
])
def test_string_to_number(item, string_value: str, int_result: int):
    try:
        int_result = int(string_value)
    except ValueError:
        int_result = int(float(string_value))

    assert item.string_to_number(string_value) == int_result


@pytest.mark.parametrize('csv_data, filename, name, price, quantity, length', [
    ('name,price,quantity\nСмартфон,100,1\n', 'dummy.csv', 'Смартфон', 100, 1, 1),
    ('name,price,quantity\nПланшет,359,2\nСмартфон,100,1\n', 'no_way.csv', 'Планшет', 359, 2, 2),
    ('name,price,quantity\nНоутбук,580,3\nПланшет,359,2\nСмартфон,100,1\n', 'soup.csv', 'Ноутбук', 580, 3, 3)
])
def test_instantiate_from_csv(mocker, csv_data, filename, name, price, quantity, length):
    mocker.patch('builtins.open', mocker.mock_open(read_data=csv_data))
    mocker.patch('os.path.join', return_value=filename)

    Item.all = []
    Item.instantiate_from_csv(filename)

    assert len(Item.all) == length

    item = Item.all[0]

    assert item.name == name
    assert item.price == price
    assert item.quantity == quantity


@pytest.mark.parametrize('class_name, name, price, quantity, expected_repr', [
    ('Item', 'Смартфон', 30_000, 7, "Item('Смартфон', 30000, 7)"),
    ('Item', 'Часы', 4_000, 12, "Item('Часы', 4000, 12)"),
    ('Item', 'Планшет', 8_000, 8, "Item('Планшет', 8000, 8)"),
])
def test_repr(item, class_name, name: str, price: int, quantity: int, expected_repr: str):
    item.name = name
    item.price = price
    item.quantity = quantity

    assert repr(item) == expected_repr


@pytest.mark.parametrize('name, expected_name', [
    ('Смартфон', 'Смартфон'),
    ('Часы', 'Часы'),
    ('Планшет', 'Планшет'),
])
def test_str(item, name: str, expected_name: str):
    item.name = name

    assert str(item) == expected_name


@pytest.mark.parametrize('this_quantity, other_quantity, expected_result', [
    (10, 13, 23),
    (7, 19, 26),
    (3, 12, 15),
])
def test_add(item, this_quantity, other_quantity, expected_result):
    item1 = item
    item1.quantity = this_quantity
    item2 = Item('', 100, other_quantity)

    assert item1 + item2 == expected_result
