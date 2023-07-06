from src.item import Item

if __name__ == '__main__':
    # file = '../src/items.csv'  # Правильный путь
    file = '../src/items2.csv'  # Путь к поврежденному файлу
    # file = '../src/item.csv'  # Путь к отсутствующему файлу
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(file)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(file)
    # InstantiateCSVError: Файл item.csv поврежден
