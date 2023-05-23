class InstantiateCSVError(Exception):

    def __str__(self):
        return f'{self.__class__.__name__}: Файл item.csv поврежден'