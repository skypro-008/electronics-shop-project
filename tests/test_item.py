
from src.item import Item
from src.item import Keyboard
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

def test_keyboard_name():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

def test_default_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"

def test_change_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"

def test_change_language_back():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    kb.change_lang()
    assert str(kb.language) == "EN"

def test_cannot_set_language_directly():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    with pytest.raises(AttributeError):
        kb.language = 'CH'