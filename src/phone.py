from items import Item

class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name=name, price=price, quantity=quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise TypeError(f"can not")



