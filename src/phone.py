from src.item import Item


class Phone(Item):
    """
    `Phone` содержит все атрибуты класса `Item` и дополнительно атрибут, содержащий количество поддерживаемых сим-карт
    """
    def __init__(self, name, price: float, quantity: int, sim_count: int) -> None:
        """
                Создание экземпляра класса phone.

                :param name: Название товара.
                :param price: Цена за единицу товара.
                :param quantity: Количество товара в магазине
                :sim_count: Количество поддерживаемых сим-карт
                """
        super().__init__(name, price, quantity)
        self.sim_count = sim_count

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.sim_count})"

    @property
    def number_of_sim(self):
        return self.sim_count

    @number_of_sim.setter
    def number_of_sim(self, sim_count):
        if sim_count > 0 and type(sim_count) is int:
            self.sim_count = sim_count
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
