from src.item import Item


def test_name_setter():
    item = Item('Телефон', 10000, 5)
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'


def test_instantiate_from_csv():
    items = Item.all
    assert len(items) == 1
    assert items[0].name == 'СуперСмарт'
    assert items[0].price == 10000
    assert items[0].quantity == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_calculate_total_price():
    item = Item('Товар', 200, 3)
    assert item.calculate_total_price() == 600


def test_apply_discount():
    item = Item('Товар', 200, 1)
    Item.pay_rate = 0.10
    assert item.apply_discount() == 20
