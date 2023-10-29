import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def sample_csv(tmpdir):
    csv_content = "name,price,quantity\nСмартфон,10000,20\nНоутбук,20000,5"
    file_path = tmpdir.join("test_items.csv")
    with open(file_path, "w") as f:
        f.write(csv_content)
    return file_path


def test_string_to_number():
    assert Item.string_to_number("100") == 100.0
    assert Item.string_to_number("3.14") == 3.14
    assert Item.string_to_number("invalid") is None


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item = Item("Смартфон", 10000, 1)
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000


def test_instantiate_from_csv(sample_csv):
    Item.all = []
    file_path = sample_csv
    Item.instantiate_from_csv(file_path)
    assert len(Item.all) == 2
    assert Item.all[0].name == "Смартфон"
    assert Item.all[0].price == 10000.0
    assert Item.all[0].quantity == 20
    assert Item.all[1].name == "Ноутбук"
    assert Item.all[1].price == 20000.0
    assert Item.all[1].quantity == 5


def test_repr():
    item = Item("Ноутбук", 156, 11)
    assert repr(item) == "Item('Ноутбук', 156, 11)"


def test_str():
    item = Item("Ноутбук", 156, 11)
    assert str(item) == "Ноутбук"


def test_add_item_and_phone():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert item1 + phone1 == 25

def test_add_item_and_item():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1 + item2 == 25

if __name__ == '__main__':
    pytest.main([__file__])
