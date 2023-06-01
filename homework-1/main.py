from src.item import Item


class Item:

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def save_price_sale(self):
        price_item = f"{self.name} {self.count * self.price}"
        price_sale = f"Цена со скидкой товара {self.name} = {price_item} "
    def save_new_class(self):
        pass

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    print(item1.calculate_total_price())  # 200000
    print(item2.calculate_total_price())  # 100000

    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount()

    print(item1.price)  # 8000.0
    print(item2.price)  # 20000

    print(Item.all)  # [<__main__.Item object at 0x000001EC6250C690>, <__main__.Item object at 0x000001EC6250C6D0>]
