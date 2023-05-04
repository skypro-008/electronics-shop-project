from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, sims):
        super().__init__(name, price, quantity)
        self.number_of_sim = sims
        self.__name = name

    def __add__(self, other):
        if other.__class__.__name__ in ["Item", "Phone"]:
            return self.quantity + other.quantity
        else:
            assert 'Не поддерживается сложение'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

