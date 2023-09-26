from src.item import Item
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
    def __str__(self):
        return self.name
    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Item):
            new_name = f"{self.name}, {other.name}"
            new_price = self.price + other.price
            new_quantity = self.quantity + other.quantity
            return new_quantity
        else:
            raise TypeError("Нельзя складывать разные телефоны!")


