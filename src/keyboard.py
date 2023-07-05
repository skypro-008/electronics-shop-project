
from src.mixing import Mixing
from src.item import Item

class Keyboard(Item, Mixing):
    """
    класс для представления товара “клавиатура”
    """


    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)






