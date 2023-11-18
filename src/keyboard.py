from src.item import Item


class Keyboard(Item):
    def __init__(self, *args):
        super().__init__(*args)
        self.__language = 'EN'

    def __str__(self):
        return f'{self.name}'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        self.__language = 'EN' if self.__language == 'RU' else 'RU'
