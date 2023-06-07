from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sims(self):
        return int(f'{self.number_of_sim}')

    @number_of_sims.setter
    def number_of_sims(self, num):
        if num > 0 and isinstance(num, int):
            self.number_of_sim = num
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')