from src.item import Item


class Phone(Item):
    """
    Наследуемый класс (класа Item)
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """
        Возвращет номер SIM-карты
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim_card) -> None:
        """
        Функция, которая проверяет количество физических SIM-карт
        (должно быть целым числом, больше нуля)
        """
        if sim_card <= 0:
            raise ValueError(
                "Количество физических SIM-карт должно быть целым числом, больше нуля."
            )
        else:
            self.__number_of_sim = sim_card

    def __str__(self):
        """
        Магический метод для отображения информации об объекте класса
        (для пользователей)
        """
        return self.name

    def __repr__(self):
        """
        Магический метод для отображения информации об объекте класса
        (для разработчиков)
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
