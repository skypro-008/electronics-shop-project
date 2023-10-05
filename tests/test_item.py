import pytest
import csv
from src.item import Item, InstantiateCSVError


@pytest.fixture
def item_fixture() -> Item:
    item = Item("Смартфон", 1000, 2)
    Item.all.append(item)
    yield item

def test_calculate_total_price(item_fixture):
    item1 = item_fixture
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 2000
    assert item2.calculate_total_price() == 100000

def test_apply_discount(item_fixture):
    item = item_fixture

    item.pay_rate = 0.8
    item.apply_discount(0.8)

    assert item.price == 800

def test_apply_discount_for_all_items(item_fixture):

    item1 = item_fixture
    item2 = Item("Ноутбук", 20000, 5)

    item1.pay_rate = 0.8
    item2.pay_rate = 0.8

    item1.apply_discount(0.8)
    item1.apply_discount(0.2)
    item2.apply_discount(0.5)

    assert item1.price == 160
    assert item2.price == 10000
    assert item1.calculate_total_price() == 256
    assert item2.calculate_total_price() == 40000

def test_item(item_fixture):
    # создание и проверка первого объекта
    item1 = item_fixture
    assert item1.name == 'Смартфон'
    assert item1.price == 1000
    assert item1.quantity == 2
    assert item1.calculate_total_price() == 2000

    # изменение свойства name
    item1.name = 'Телефон'
    assert item1.name == 'Телефон'

    # создание и проверка второго объекта с длинным name
    big_item = Item('СуперСмартфон', 5000, 10)
    Item.all.append(big_item)
    assert big_item.name == 'СуперСмартфон'

    # создание объектов из файла csv
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 9
    item2 = Item.all[0]
    assert item2.name == 'Телефон'
    assert item2.price == 1000
    assert item2.quantity == 2
    assert item2.calculate_total_price() == 2000

    # проверка метода string_to_number
    assert Item.string_to_number('5') == 5.0
    assert Item.string_to_number('5.0') == 5.0
    assert Item.string_to_number('5.5') == 5.5

def test___repr__():
    item = Item("Ноутбук", 20000, 5)
    assert item.__repr__() == "Item('Ноутбук', 20000, 5)"

def test___str__():
    item = Item("Ноутбук", 20000, 5)
    assert item.__str__() == 'Ноутбук'


def test_instantiate_from_csv_file_not_found():
    '''Тест для несуществующего файла'''
    assert Item.instantiate_from_csv() == None
    try:
        Item.instantiate_from_csv()
    except FileNotFoundError as e:
        assert str(e) == 'Отсутствует файл items.csv'

def test_instantiate_from_csv_invalid_data(tmp_path):
    '''Тест для поврежденнного файла'''
    # Создаем временный файл item.csv для тестирования, в котором есть некорректные данные
    file_data = "name,price,quantity\nТовар1,2.0,3.0\nТовар2,invalid,4.0\nТовар3,1.0,lol\n"
    file_path = tmp_path / "item.csv"
    with open(file_path, "w", encoding='windows-1251') as f:
        f.write(file_data)

    with pytest.raises(InstantiateCSVError) as exc_info:
        Item.instantiate_from_csv(str(file_path))
    assert str(exc_info.value).startswith('Файл item.csv поврежден:')

