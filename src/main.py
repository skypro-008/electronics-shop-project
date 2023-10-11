from classes import Warehouse, Item


if __name__ == '__main__':
    item1 = Item("Смартфон", 10000)
    item2 = Item("Ноутбук", 20000)

    warehouse = Warehouse()
    warehouse.add_new_item(item1, 20)
    warehouse.add_new_item(item2, 5)

    Item.pay_rate = 0.8
    item1.apply_discount()

    print(item1.price)
    print(item2.price)

    print(warehouse.all_items)