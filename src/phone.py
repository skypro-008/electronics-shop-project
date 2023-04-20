from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim_card: int) -> None:
        super().__init__(name, price, quantity)

        if not isinstance(sim_card, int) or sim_card < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

        self.__number_of_sim = sim_card

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):

        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim >= 1:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        return
