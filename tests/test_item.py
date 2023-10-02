
from src.item import Item
from src.phone import Phone


phone = Item('Телефон', 100, 5)
Item.pay_rate = 5


def test_calculate_total_price():
    assert phone.calculate_total_price() == 500


def test_apply_discount():
    phone.apply_discount()
    assert phone.price == 500


def test_string_to_number():
    assert Item.string_to_number('99.9') == 99
    assert Item.string_to_number('99') == 99


def test_name_setter():
    test = Item('Телевизор', 500, 1)
    test.name = 'Тостер'
    assert test.name == 'Тостер'
    test.name = 'мп3'
    assert test.name == 'мп3'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('/Users/mac/Dev/electronics-shop-project'
                              '/src/items.csv')
    assert len(Item.all) == 0


def test_repr():
    phone = Item('Телефон', 3, 1)
    assert repr(phone) == "Item('Телефон', 3, 1)"


def test_str():
    phone = Item('Телефон', 5, 2)
    assert str(phone) == 'Телефон'


def test_add():
    dvd = Item("dvd", 9.99, 2)
    iphone = Phone("iphone", 199.99, 2, 1)
    assert dvd + iphone == 4