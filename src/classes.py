from exceptions import ItemNotFoundException


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{__class__.__name__}: name="{self.name}, price="{self.price}"'

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара."""
        self.price = self.price * Item.pay_rate


class Warehouse:
    def __init__(self):
        """Словарь, содержащий все товары. Должен иметь вид:
        {'item': Item('something', 1.0), 'amount': 1}"""
        self.all_items = {}

    def add_new_item(self, item, amount):
        """Добавление нового товара на склад"""
        self.all_items[item.name] = {'item': item, 'amount': amount}

    def add_items_by_name(self, item_name, amount):
        """Добавление некоторого количества товара к уже существующему такому же по названию"""
        if item_name in self.all_items:
            self.all_items[item_name]['amount'] += amount
        else:
            """Бросаю исключение, потому что сообщение при этом будет для разработчиков. 
            Подразумевается, что из пользовательского интерфейса невозможно будет добавить 
            товар с произвольным названием, тк обычно это какая-нибудь кнопка с названием
            товара. Конечно, в реальных условиях нужно будет опираться на ТЗ, здесь об этом не было
            сказано, я принял такое решение логически"""
            raise ItemNotFoundException(f"Warehouse haven't item with name '{item_name}'")

    def del_items_by_name(self, item_name, amount):
        """Удаление некоторого количества товара по названию"""
        if amount > self.all_items[item_name]['amount']:
            print('Too much. Try to get fewer items!')
        else:
            self.all_items[item_name]['amount'] -= amount
            """Если остаётся ноль товаров, можно добавить их в архив, чтобы помнить, что они были.
            Я же просто удалю позицию со склада, например"""
            if self.all_items[item_name]['amount'] == 0:
                self.all_items.pop(item_name)

    def get_price_all_items_by_name(self, item_name):
        """Получить общую стоимость товара по его названию"""
        if item_name in self.all_items:
            return self.all_items[item_name]['item'].price * self.all_items[item_name]['amount']
        else:
            raise ItemNotFoundException(f"Warehouse haven't item with name '{item_name}'")
