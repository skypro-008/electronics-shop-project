from src.item import Item


class Phone(Item):
    """
    наследует name, price, quantity от класса Item и инициализиурет
    свой индивидульный параметр number_of_sim
    """
    def __init__(self, name: str, price: int, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        выводит название класса, имя продукта, цену, кол-во товара и кол-во СИМ-карт
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        """
        выводит название товара
        """
        return f'{self.name}'

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        self.__number_of_sim = value






