import csv
from pathlib import Path
from src.item import Item
class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim:int) -> None:
        Item.__init__(self, name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Phone и Item ')
        return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'


    def number_of_sim(number_of_sim: int):
        if int(number_of_sim) != number_of_sim or number_of_sim <= 0:
            raise ValueError('Количество сим карт должно быть целым неотрицательным числом')
        return number_of_sim

