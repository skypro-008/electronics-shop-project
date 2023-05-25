from items import Item

class Phone(Item):

    def __init__(self, name, price, quantity, __number_of_sim):
        super().__init__(name=name, price=price, quantity=quantity)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        if not isinstance(new_number_of_sim, int) or new_number_of_sim <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.number_of_sim = new_number_of_sim


    def __add__(self, other):
        if isinstance(other, Phone):
            total_quantity = self.quantity + other.quantity
            return total_quantity
        elif isinstance(other, Item):
            total_quantatity = self.quantity +other.quantity
            return total_quantatity
