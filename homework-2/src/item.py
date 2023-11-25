class Item:
    def __init__(self, name, price):
        self.__name = name
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        items = []
        with open('src/items.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = cls(row['name'], row['price'])
                items.append(item)
        return items

    @staticmethod
    def string_to_number(string):
        return int(string)