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
def test_string_to_number(item, string_value, int_result):
    try:
        int_result = int(string_value)
    except ValueError:
        int_result = int(float(string_value))

    assert item.string_to_number(string_value) == int_result


@pytest.mark.parametrize('csv_data, filename, name, price, quantity, lenght', [
    ('name,price,quantity\nСмартфон,100,1\n', 'dummy.csv', 'Смартфон', '100', '1', 1),
    ('name,price,quantity\nПланшет,359,2\nСмартфон,100,1\n', 'no_way.csv', 'Планшет', '359', '2', 2),
    ('name,price,quantity\nНоутбук,580,3\nПланшет,359,2\nСмартфон,100,1\n', 'soup.csv', 'Ноутбук', '580', '3', 3)
])
def test_instantiate_from_csv(item, mocker, csv_data, filename, name, price, quantity, lenght):
    mocker.patch('builtins.open', mocker.mock_open(read_data=csv_data))
    mocker.patch('os.path.join', return_value=filename)

    Item.all = []
    Item.instantiate_from_csv(filename)

    item.name = name
    item.price = price
    item.quantity = quantity

    assert len(Item.all) == lenght
    assert item.name == name
    assert item.price == price
    assert item.quantity == quantity


