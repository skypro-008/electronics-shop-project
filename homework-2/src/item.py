import csv

class Item:
    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self._name = value[:10]
        else:
            self._name = value

    @classmethod
    def instantiate_from_csv(cls):
        items = []
        with open('src/items.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = cls(row['id'], row['name'], row['price'])
                items.append(item)
        return items

    @staticmethod
    def string_to_number(string):
        return int(string)