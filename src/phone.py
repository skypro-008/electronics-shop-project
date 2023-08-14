from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, count_sim: int):
        super().__init__( name, price, quantity)
        if isinstance(count_sim, int) and count_sim > 0:
            self.__count_sim = count_sim
        else:
            raise Exception('Количество физических SIM-карт должно быть целым числом больше нуля.')


    @property
    def count_sim(self):
        return self.__count_sim


    @count_sim.setter
    def count_sim(self, count_sim):
        if isinstance(count_sim, int) and count_sim > 0:
            self.__count_sim = count_sim
        else:
            raise Exception('Количество физических SIM-карт должно быть целым числом больше нуля.')


    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.count_sim})"


    def __str__(self):
        return f'{self.name}'


