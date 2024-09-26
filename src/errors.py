class InstantiateCSVError(Exception):
    """Исключение, которое выбрасывается при ошибке чтения файла item.csv"""
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = "Файл item.csv поврежден"
