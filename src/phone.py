from src.item import Item


class Phone(Item):

    def __int__(self, name, price, quantity, count_sim_card):
        super().__init__(name, price, quantity)
        self.count_sim_card = count_sim_card
