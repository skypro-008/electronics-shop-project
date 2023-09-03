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

    def __setattr__(self, key, value):
        """
        Отбрасывает недопустимые данные для физических SIM-карт
        """
        if key == 'number_of_sim' and (value <= 0 or not isinstance(value, int)):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            object.__setattr__(self, key, value)
