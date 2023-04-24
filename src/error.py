class InstantiateCSVError(Exception):
    """Общий класс исключения для скриптов"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка '

    def __str__(self):
        return self.message


class FileNotFoundError(InstantiateCSVError):
    """Класс исключения при отсутствии файла"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Отсутствует файл который item.csv.'


class InstantiateCSVError(InstantiateCSVError):
    """Класс исключения при повреждении csv файла"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден.'


class InstantiateCSV:
    """Класс для работы """

    def __init__(self, filename: str):
        if not filename:  # Если файла нет
            raise NoFile
        elif filename[0:2] != '#!':  # Если файл битый
            raise FileIsBed
        else:
            self.filename = filename

    def evaluate(self):
        # Код исполнения скрипта
        pass