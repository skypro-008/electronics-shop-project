from src.item import Item


class Keyboard(Item):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__( name, price, quantity)
        self._language = 'EN'



    def  __str__(self):
        return f'{self.name}'

    @property
    def language(self):
        return self._language


    def change_lang(self):

        if self._language == 'RU':
            self._language = 'EN'
        elif self._language == 'EN':
            self._language = 'RU'





