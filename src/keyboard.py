from src.item import Item

class MixinLanguage:
    """класс mixin с дополнительным функционалом по хранению и изменению раскладки клавиатуры"""

    __language = "EN"

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, new_language):
        # Здесь можно добавить дополнительную логику, если необходимо
        self._language = new_language


    def change_lang(self) -> None:
        """Метод для изменения языка"""

        if self.language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"




class Keyboard(Item, MixinLanguage):
    """Класс для товара 'клавиатура' """
    pass