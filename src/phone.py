from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int = 1):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"'{self.name}', "
                f"{self._price}, "
                f"{self._quantity}, "
                f"{self._number_of_sim}"
                ")")

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if isinstance(value, int) and value > 0:
            self._number_of_sim = value
            return

        raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

