
from src.item import Item

def test_calculate_total_price():
    item = Item("Test", 10, 5)
    assert item.calculate_total_price() == 50

def test_apply_discount():
    item = Item("Test", 100, 1)
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 80

def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert len(items) == 3

def test_string_to_number():
    result = Item.string_to_number("100")
    assert result == 100

def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'