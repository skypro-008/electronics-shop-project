from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        if number_of_sim <= 0:
            raise ValueError('Количество физических SIM - карт должно быть целым числом больше нуля')
        else:
            self.number_of_sim = number_of_sim
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

