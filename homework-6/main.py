from src.item import Item, filename

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv("ddd")
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(filename)
    # InstantiateCSVError: Файл item.csv поврежден
