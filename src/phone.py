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
        self.__number_of_sim = number_of_sim


    def __repr__(self) -> str:
        """Метод для отображения информации об объекте класса в режиме отладки (для разработчиков)"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

# Геттер для number_of_sim
    @property
    def number_of_sim(self):
        """Возвращает информацию о поддерживаемых сим-картах. К атрибуту можно обращаться без вызова."""
        return self.__number_of_sim

    # Cеттер для number_of_sim
    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """Сеттер проверяет, что количество физических SIM-карт должно быть целым числом больше нуля."""
        if number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')