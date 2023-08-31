from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        """
        Инициализация для класса Phone
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):

        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        """
        Сложение количества товара экземпляров классов Phone и Item
        """
        if isinstance(other, Item):

            return self.quantity + other.quantity

    # def __set__(self, number):
    #     if number > 0 and type(number) is int:
    #         self.number_of_sim = number
    #     else:
    #         raise "ValueError: Количество физических SIM-карт должно быть целым числом больше нуля."
