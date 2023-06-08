from src.item import Item
class Phone(Item):
    """
    Класс для представления нового товара в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра дочернего класса phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param sim_cards: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.name = name
        self.number_of_sim = number_of_sim


    def __repr__(self) -> str:
        """Метод для отображения информации об объекте класса в режиме отладки (для разработчиков)"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


    @classmethod
    def number_of_sim(cls, number_of_sim):
        """Метод для отображения информации о поддерживаемых сим-картах"""
        if number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
