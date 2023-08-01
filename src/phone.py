from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        """
        Создание экземпляра класса Phone
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """Вывод информации для разработчика"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

