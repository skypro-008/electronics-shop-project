class KeyBoard:
    def __init__(self, language: str, price: float, quantity: int):
        self.language = language
        self.price = price
        self.quantity = quantity


kb = KeyBoard('Dark Project KD87A', 9600, 5)
print(kb.__dict__)