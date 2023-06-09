import pytest
import csv
from src.item import Item, InstantiateCSVError


def test_calculate_total_price(item_smartphone_10000_20,
                               item_notebook_20000_5,
                               item_notebook_lenovo_0_0,
                               item_notebook_aser_minus_25000_minus_15):
    """Тест расчёта общей стоимости конкретного товара"""
    assert item_smartphone_10000_20.calculate_total_price() == 200000
    assert item_notebook_20000_5.calculate_total_price() == 100000
    assert item_notebook_lenovo_0_0.calculate_total_price() == 0
    assert item_notebook_aser_minus_25000_minus_15.calculate_total_price() == 'Проверьте товары. Цена или количество не должны быть отрицательными.'


def test_apply_discount(pay_rate_1,
                        item_smartphone_10000_20,
                        item_notebook_20000_5,
                        item_notebook_lenovo_0_0,
                        item_notebook_aser_minus_25000_minus_15):
    """Тест установки скидки для конкретного товара"""
    item_smartphone_10000_20.pay_rate = pay_rate_1
    item_notebook_20000_5.pay_rate = pay_rate_1
    item_notebook_lenovo_0_0.pay_rate = pay_rate_1
    assert item_smartphone_10000_20.apply_discount() == 8000
    assert item_notebook_20000_5.apply_discount() == 16000
    assert item_notebook_lenovo_0_0.apply_discount() == 'Проверьте значения скидки или цены. Одно из них равно нулю.'
    assert item_notebook_aser_minus_25000_minus_15.apply_discount() == 'Проверьте значения скидки или цены. Одно из них меньше нуля'


def test_repr(item_smartphone_10000_20, item_notebook_20000_5, item_notebook_lenovo_0_0):
    """
    Тест на правильность преобразования объекта Item в строку для вывода в отладке
    """
    assert item_smartphone_10000_20.__repr__() == "Item('Смартфон', 10000, 20)"
    assert item_notebook_20000_5.__repr__() == "Item('Ноутбук', 20000, 5)"
    assert item_notebook_lenovo_0_0.__repr__() == "Item('Ноутбук_lenovo', 0, 0)"


def test_str(item_smartphone_10000_20, item_notebook_20000_5, item_notebook_lenovo_0_0):
    """
    Тест на правильность преобразования объекта Item в строку
    для представления элемента класса пользователю
    """
    assert item_smartphone_10000_20.__str__() == 'Смартфон'
    assert item_notebook_20000_5.__str__() == 'Ноутбук'
    assert item_notebook_lenovo_0_0.__str__() == 'Ноутбук_lenovo'


def test_get_all_items(item_smartphone_10000_20, item_notebook_20000_5):
    """ Тестируем возвращаемость списка товаров"""
    Item.all = [item_smartphone_10000_20.__repr__(), item_notebook_20000_5.__repr__()]
    assert Item.get_all_items() == ["Item('Смартфон', 10000, 20)",
                                    "Item('Ноутбук', 20000, 5)"]


def test_get_count_items(test_all_items):
    """Тест подсчёта общего количества товаров"""
    Item.all = test_all_items
    assert Item.get_count_items() == 2


def test_get_name(item_notebook_lenovo_0_0):
    assert item_notebook_lenovo_0_0.name == 'Ноутбук_lenovo'


def test_set_name_valid(item_notebook_lenovo_0_0):
    item_notebook_lenovo_0_0.name = 'Lenovo'
    assert item_notebook_lenovo_0_0.name == 'Lenovo'


def test_set_name_invalid(item_notebook_lenovo_0_0):
    with pytest.raises(Exception) as exc_info:
        item_notebook_lenovo_0_0.name = '12345678901'
    assert str(exc_info.value) == 'Длина товара превышает 10 символов.'
    assert item_notebook_lenovo_0_0.name == 'Ноутбук_lenovo'


def test_instantiate_csv_error():
    """Проверка текста ошибки класса InstantiateCSVError"""
    e = InstantiateCSVError()
    assert e.message == 'Файл .cvs повреждён: не хватает колонок.'
    assert e.__str__() == 'Файл .cvs повреждён: не хватает колонок.'


def test_not_file_instantiate_from_csv():
    """Проверка загрузки данных из несуществующего файла"""
    with pytest.raises(FileNotFoundError) as e:
        Item.instantiate_from_csv("not_found_items.csv")
    assert "No such file or directory" in str(e.value)


def test_wrong_file_instantiate_from_csv():
    """Проверка загрузки данных из файла с недостающим количеством колонок или повреждённым"""
    with pytest.raises(InstantiateCSVError) as e:
        Item.instantiate_from_csv("../tests/without_colum_items.csv")
    assert 'Файл .cvs повреждён: не хватает колонок.' in str(e.value)


def test_incorrect_headers_instantiate_from_csv(tmp_path):
    """Проверяем заголовки в файле csv"""
    # Создаем временный файл CSV с неправильными заголовками
    csv_file = tmp_path / "test.csv"
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "price"])
        writer.writerow(["item1", "10.5"])
        writer.writerow(["item2", "22.2"])

    # Проверяем, что метод instantiate_from_csv вызывает исключение при чтении этого файла
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(csv_file)


def test_instantiate_from_csv_with_wrong_data(tmp_path):
    """Проверяем чтение данных из строки по заголовкам из cvs"""
    # Создаем временный файл CSV с неправильными данными
    csv_file = tmp_path / "items.csv"
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "price", "quantity"])
        writer.writerow(["item1", "10.5", "abc"])  # неправильное значение количества

    # Получаем список объектов Item из CSV файла, ожидаем ошибку при чтении данных
    with pytest.raises(ValueError):
        Item.instantiate_from_csv(csv_file)


def test_instantiate_from_csv(tmp_path):
    """Проверяем получение данных из csv"""
    # Создаем временный файл CSV
    csv_file = tmp_path / "items.csv"
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "price", "quantity"])
        writer.writerow(["item1", "10.5", "20"])
        writer.writerow(["item2", "22.2", "30"])

    # Получаем список объектов Item из CSV файла
    items = Item.instantiate_from_csv(csv_file)

    # Проверяем, что список не пустой
    assert items

    # Проверяем, что все объекты имеют нужные атрибуты
    for item in items:
        assert hasattr(item, "name")
        assert hasattr(item, "price")
        assert hasattr(item, "quantity")

    # Проверяем значения атрибутов первого объекта
    assert items[0].name == "item1"
    assert items[0].price == 10.5
    assert items[0].quantity == 20

    # Проверяем значения атрибутов второго объекта
    assert items[1].name == "item2"
    assert items[1].price == 22.2
    assert items[1].quantity == 30

    # Проверяем, что создался список объектов Item
    assert isinstance(Item.all, list)
    assert len(Item.all) == 2


def test_string_to_number(strings):
    """
    Проверка перевода строки в число
    """
    string_1, string_2, string_3 = strings.split(', ')

    assert Item.string_to_number(string_1) == 0
    assert Item.string_to_number(string_2) == 5
    assert Item.string_to_number(string_3) == 5


def test_add(item_notebook_lenovo_0_0, item_smartphone_10000_20, item_notebook_20000_5):
    """
    Сложение количества товаров
    """
    assert item_notebook_lenovo_0_0.__add__(item_smartphone_10000_20) == 20
    assert item_smartphone_10000_20.__add__(item_notebook_20000_5) == 25


def test_fail_add(item_notebook_lenovo_0_0):
    """
    Нельзя складывать экземпляры Item с экземплярами не Item классов.
    """

    class Test:
        def __init__(self):
            self.quantity = 10

    test = Test()
    with pytest.raises(ValueError) as excinfo:
        item_notebook_lenovo_0_0.__add__(test)
    assert str(excinfo.value) == 'Можно складывать только экземпляры классов Item'
