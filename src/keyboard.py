from src.item import Item

class Keyboard(Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.language = 'EN'

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
            return self
        else:
            self.language = 'EN'
            return self
