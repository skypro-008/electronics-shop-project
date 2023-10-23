from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        if number_of_sim == 0:
            raise ValueError('Error')
        self.number_of_sim = number_of_sim

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
