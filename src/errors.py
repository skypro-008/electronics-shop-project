# -*- coding: utf-8 -*-
class InstantiateCSVError(Exception):
    """
    Класс-исключение для ошибок при работе с файлом csv
    """
    def __init__(self, *args):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = "Файл item.csv поврежден"

    def __str__(self):
        return f'{self.message}'