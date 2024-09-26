import csv

data = [
    {"name": "Продукт 1", "price": "10.99", "quantity": "5"},
    {"name": "Продукт 2", "price": "19.99", "quantity": "8"},
    {"name": "Продукт 3", "price": "5.00", "quantity": "12"},
]

filename = 'items.csv'

with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "price", "quantity"])
    writer.writeheader()
    writer.writerows(data)

print(f"Файл {filename} успешно создан.")