from src.item import Item
class Phone(Item):
    def __init__(self,name,price,quantity,number_of_sim):
        super().__init__(name,price,quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if not isinstance(self,Item) and not isinstance(other,Phone):
            return ValueError('Складывать можно только объекты Item и Phone классов')
        else:
            return int(self.quantity) + int(other.quantity)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'