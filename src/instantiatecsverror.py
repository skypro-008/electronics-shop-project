class InstantiateCSVError(Exception):
    """Общий класс исключения для скриптов"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка '

    def __str__(self):
        return self.message


class ShellScriptEmpty(InstantiateCSVError):
    """Класс исключения при отсутствии файла"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Отсутствует файл который item.csv.'


class ShellScriptShebang(InstantiateCSVError):
    """Класс исключения при повреждении csv файла"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден.'


class InstantiateCSV:
    """Класс для работы """

    def __init__(self, script: str):
        if not script:  # Если скрипт пустой
            raise ShellScriptEmpty
        elif script[0:2] != '#!':  # Если отсутствует shebang
            raise ShellScriptShebang
        else:
            self.script = script

    def evaluate(self):
        # Код исполнения скрипта
        pass