from src.item import Item


def test_item():
    """
    Тестирование создание экземпляра item
    """
    item = Item("Телевизор", 100_000, 3)
    assert item.name == "Телевизор"
    assert item.price == 100_000
    assert item.quantity == 3


def test_calculate_total_price():
    """
    Тестирование общей стоимости товара в магазине
    """
    item = Item("Телевизор", 100_000, 3)
    assert item.calculate_total_price() == 300_000


def test_apply_discount():
    """
    Проверка применения скидки
    """
    item = Item("Телевизор", 100_000, 3)
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 50_000


def test_name():
    """
    Проверка на превышение 10 символов в name
    """
    item = Item('Телефон', 10000, 5)
    item.name = "СуперСмартфон"
    assert item.name == 'СуперСмарт'
def test_instantiate_from_csv():
    """
    Проверка инифиализации экземпляра класса `Item`
    """
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    test_item = Item.all[2]
    assert test_item.price == 10
    assert test_item.name == "Кабель"

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5