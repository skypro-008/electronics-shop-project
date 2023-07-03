
from src.item import Item
class Phone(Item):
    
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"


    @property
    def number_of_sim(self):
        """
        Выводит количество симкарт для объекта класса Phone
        """
        return self.__number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int):
        """
        Присваивает новое количество симкарт, количество симкарт должно быть больше нуля
        """
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")


