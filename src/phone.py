from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_sim_cards: int):
        super().__init__(name, price, quantity)
        self.number_sim_cards = number_sim_cards

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_sim_cards})"

    @property
    def number_sim_cards(self):
        """Геттер для кол-ва симкарт"""
        return self.__number_sim_cards

    @number_sim_cards.setter
    def number_sim_cards(self, new_number):
        """Cеттер для кол-ва симкарт"""
        if new_number > 0 and isinstance(new_number, int):
            self.__number_sim_cards = new_number
        raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
