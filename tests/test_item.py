from src.item import Item

# Создаем экземпляр товара
item = Item("Название товара", 1000, 5)


# Проверяем, что атрибуты класса Item были установлены правильно
assert item.name == "Название товара"
assert item.price == 1000
assert item.quantity == 5
assert item.discount_level == 1.0
assert item.instances == 0

# Применяем скидку к товару
item.apply_discount(0.85)

# Проверяем, что уровень скидки был успешно применен
assert item.discount_level == 0.85

# Добавляем еще один экземпляр товара
item.add_instance()

# Проверяем, что количество экземпляров товара увеличилось
assert item.instances == 1
''' верно хоть?'''