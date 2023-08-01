from src.item import Item


class Keyboard(Item):
    """Класс, описывающий сущность - клавиатура"""

    def __init__(self, name: str, price: float, quantiti: int) -> None:
        """Конструктор класса"""

        super().__init__(name, price, quantiti)
