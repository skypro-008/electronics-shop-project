from src.item import Item

obj1 = Item("Смартфон", 10000, 20)
obj2 = Item("Ноутбук", 20000, 5)

def test_Item_init():
    """
    Тест создания экземпляра класса item.

    :param name: Название товара.
    :param price: Цена за единицу товара.
    :param quantity: Количество товара в магазине.
     """
    assert obj1.name == "Смартфон"
    assert obj1.price == 10000
    assert obj1.quantity == 20
    assert obj2.name == "Ноутбук"
    assert obj2.price == 20000
    assert obj2.quantity == 5

def test_calculate_total_price():
    """
    Тест рассчета общей стоимости конкретного товара в магазине.

    """
    obj1.calculate_total_price()
    obj2.calculate_total_price()
    assert obj1.total_price == 200000
    assert obj2.total_price == 100000

def test_apply_discount():
    """
    Тест применения установленной скидку для конкретного товара.
    """
    obj1.pay_rate = 0.8
    obj1.apply_discount()
    obj2.apply_discount()
    assert obj1.price == 8000
    assert obj2.price == 20000

#############################################