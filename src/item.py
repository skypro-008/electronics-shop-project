import csv


class InstantiateCSVError(Exception):
    def __init__(self, message="Файл item.csv поврежден"):
        self.message = message
        super().__init__(self.message)


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    @property
    def name(self):
        """Геттер для названия товара."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Сеттер для названия товара с проверкой длины."""
        if len(value) > 10:
            print("Длина наименования товара превышает 10 символов.")
            value = value[:10]
        self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate



    @classmethod
    def instantiate_from_csv(cls, file_path: str = 'item.csv') -> None:
        """
        Создает экземпляры класса Item из данных CSV-файла.
        """
        cls.all.clear()
        required_columns = {'name', 'price', 'quantity'}

        try:
            with open(file_path, newline='', encoding='cp1251') as csvfile:
                reader = csv.DictReader(csvfile)

                missing_columns = required_columns - set(reader.fieldnames)
                if missing_columns:
                    raise InstantiateCSVError(f"Файл item.csv поврежден. Отсутствуют колонки: {', '.join(missing_columns)}")

                for row in reader:
                    try:
                        name = row['name']
                        price = float(row['price'])
                        quantity = int(row['quantity'])
                        cls(name, price, quantity)
                    except ValueError as e:
                        print(f"Ошибка в данных строки {row}: {e}")
        except FileNotFoundError:
            print(f"Отсутствует файл {file_path}")
        except InstantiateCSVError as e:
            print(e)

    @staticmethod
    def string_to_number(s: str) -> int:
        """
        Конвертирует строку в число.
        """
        return int(float(s))

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity




