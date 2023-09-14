import csv

from src.item import Item


def test_calculate_total_price():
    test_item = Item('Товар', 200, 1)
    assert test_item.calculate_total_price() == 200


def test_apply_discount():
    test_item = Item('Товар', 200, 1)
    Item.pay_rate = 0.10
    assert test_item.apply_discount() == 20


def test_instantiate_from_csv(tmp_path):
    test_csv_file = tmp_path / "items.csv"
    with open(test_csv_file, 'w',encoding='windows-1251', newline='') as csvfile:
        fieldnames = ['name', 'price', 'quantity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'name': 'Тестовый товар 1', 'price': '100', 'quantity': '5'})

    Item.instantiate_from_csv(test_csv_file)
    items = Item.all
    assert len(items) == 8
    assert items[0].quantity == 1
    assert items[1].quantity == 3
