class InstantiateCSVError(Exception):
    def __init__(self):
        print("Файл item.csv поврежден")

    def __repr__(self):
        return "Файл item.csv поврежден"
