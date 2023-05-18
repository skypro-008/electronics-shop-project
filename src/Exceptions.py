class InstantiateCSVError(Exception):
    def __init__(self):
        print("Файл items.csv поврежден")

    def __repr__(self):
        return "Файл items.csv поврежден"
