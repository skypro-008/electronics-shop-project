class InstantiateCSVError(Exception):
    def __init__(self, text):
        self.message = text


class EmptyFile(Exception):
    def __init__(self, text):
        self.message = text


# try:
#     isempty = os.stat(cls.items_csv).st_size == 0
# except EmptyFile:
#     raise EmptyFile('Файл items.csv пустой')