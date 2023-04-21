from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim #количество поддерживаемых сим карт

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f"{self.name}"

    def __radd__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            return 'Складывать можно только объекты Item и дочерние от них.'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            return 'Складывать можно только объекты Item и дочерние от них.'
