
class Mixing:
    """
    Класс для реализации дополнительного функционала по хранению и
    изменению раскладки клавиатуры объекта класса Keyboard.
    Язык по умолчанию (при инициализации) - английский (`EN`)
    """


    def __init__(self):
        self.__language = 'EN'


    @property
    def language(self):
        return self.__language


    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self
