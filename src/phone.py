from src.item import Item




class Phone(Item):


    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):

        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, add_sim: int):

        if add_sim >= 0 and isinstance(add_sim, int):
            self.__number_of_sim = add_sim

        else:
            raise ValueError('Неверное количество сим')



    def __repr__(self) -> str:
        return f'{self.__class__.__name__}{self.name, self.price, self.quantity, self.number_of_sim}'

    ##if not isinstance(other, Item):
            #raise ValueError('нельзя складывать')
        #return int(self.quantity) + int(other.quantity)





