import pytest
from src.keyboard import Keyboard

@pytest.fixture
def item_fixture() -> Keyboard:
    item = Keyboard("Dark Project KD87A", 1000, 2)
    Keyboard.all.append(item)
    yield item

def test_calculate_total_price(item_fixture):
    item1 = item_fixture
    item2 = Keyboard("Dark Project KD87A", 20000, 5)

    assert item1.calculate_total_price() == 2000
    assert item2.calculate_total_price() == 100000

def test_apply_discount(item_fixture):
    item = item_fixture

    item.pay_rate = 0.8
    item.apply_discount(0.8)

    assert item.price == 800

def test_apply_discount_for_all_items(item_fixture):
    item1 = item_fixture
    item2 = Keyboard("Dark Project KD87A", 20000, 5)

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
    item1 = item_fixture
    assert item1.name == 'Dark Project KD87A'
    assert item1.price == 1000
    assert item1.quantity == 2
    assert item1.calculate_total_price() == 2000

    item1.name = 'Dark Project KD87A'
    assert item1.name == 'Dark Proje'

    big_item = Keyboard('Dark Project KD87A', 5000, 10)
    Keyboard.all.append(big_item)
    assert big_item.name == 'Dark Project KD87A'

    assert len(Keyboard.all) == 4
    item2 = Keyboard.all[0]
    assert item2.name == 'Dark Proje'
    assert item2.price == 1000
    assert item2.quantity == 2
    assert item2.calculate_total_price() == 2000

    # проверка метода string_to_number
    assert Keyboard.string_to_number('5') == 5.0
    assert Keyboard.string_to_number('5.0') == 5.0
    assert Keyboard.string_to_number('5.5') == 5.5

def test___repr__():
    item = Keyboard("Dark Project KD87A", 20000, 5)
    assert item.__repr__() == "Item('Dark Project KD87A', 20000, 5)"

def test___str__():
    item = Keyboard("Dark Project KD87A", 20000, 5)
    assert item.__str__() == 'Dark Project KD87A'

def test_change_lang(item_fixture):
    item = item_fixture
    assert item.language == 'EN'
    item.change_lang()
    assert item.language == 'RU'
    item.change_lang()
    assert item.language == 'EN'

    with pytest.raises(ValueError):
        item._lang = 'CH'
        item.change_lang()