from src.item import Item


class MixinLanguage:
    def __init__(self, name: str, price: float, quantity: int, language: str = "EN") -> None:
        """Инициализация класса клавиатура"""
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        """Вывод на печать"""
        return self.__language

    @language.setter
    def language(self, change_language):
        """Установить значение language"""
        if change_language in ["EN", "RU"]:
            self.__language = change_language
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        """Изменить значение на EN или RU"""
        if self.language == "EN":
            self.language = "RU"
            return self
        self.language = "EN"
        return self


class Keyboard(MixinLanguage, Item):
    pass