from src.item import Item


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


def test_repr_str(item_smartphone_10000_20, item_notebook_20000_5):
    """
    Тест на правильность преобразования объекта Item в строку
    """
    assert str(item_smartphone_10000_20) == '[Item: name=Смартфон, price=10000, quantity=20]'
    assert str(item_notebook_20000_5) == '[Item: name=Ноутбук, price=20000, quantity=5]'


def test_get_all_items(item_smartphone_10000_20, item_notebook_20000_5):
    """ Тестируем возвращаемость списка товаров"""
    Item.all = [item_smartphone_10000_20.__repr__(), item_notebook_20000_5.__repr__()]
    assert Item.all == ['[Item: name=Смартфон, price=10000, quantity=20]',
                        '[Item: name=Ноутбук, price=20000, quantity=5]']


def test_get_count_items(test_all_items):
    """Тест подсчёта общего количества товаров"""
    Item.all = test_all_items
    assert Item.get_count_items() == 2


def test_name(item_notebook_lenovo_0_0, item_smartphone_10000_20):
    """ Тест проверки наименования """
    assert item_notebook_lenovo_0_0.name == 'Наименование должно быть меньше 10 символов.'
    assert item_smartphone_10000_20.name == "Смартфон"
    item_smartphone_10000_20.name = "Смартфон_S"
    assert item_smartphone_10000_20.name == "Смартфон_S"
    item_smartphone_10000_20.name = "Смартфон"


def test_instantiate_from_csv():
    """ Проверка создания объектов из файла """
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5 # в файле 5 записей с данными по товарам


def test_string_to_number(strings):
    """
    Проверка перевода строки в число
    """
    string_1, string_2, string_3 = strings.split(', ')

    assert Item.string_to_number(string_1) == 0
    assert Item.string_to_number(string_2) == 5
    assert Item.string_to_number(string_3) == 5
