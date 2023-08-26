"""Здесь надо написать тесты с использованием pytest для модуля item."""

# Импорт класса Item из вашего модуля
from src.item import Item

# Тест на расчет общей стоимости товара
def test_calculate_total_price():
    item = Item("Товар 1", 100, 5)
    total_price = item.calculate_total_price()
    assert total_price == 500  # Проверяем, что общая стоимость рассчитана правильно

# Тест на применение скидки
def test_apply_discount():
    item = Item("Товар 2", 200, 3)
    item.apply_discount()
    assert item.price == 200  # Проверяем, что цена уменьшилась на 20% после скидки

# Тест на добавление товара в атрибут all
def test_add_item_to_all():
    item = Item("Товар 3", 50, 10)
    assert item in Item.all  # Проверяем, что созданный товар добавлен в список всех товаров

# Тест для применения скидки
def test_apply_discount_rate():
    item = Item("Товар 4", 200, 3)
    item.pay_rate = 0.9  # Устанавливаем скидку 10%
    item.apply_discount()
    assert item.price == 180


