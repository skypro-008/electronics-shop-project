"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src import item


def item_item():
    return item.Item("Смартфон", 10000, 20)


def test___init__():
    assert item_item().__init__("Смартфон", 10000, 20) is None


def test_calculate_total_price():
    assert item_item().calculate_total_price() == 200000


def test_apply_discount():
    assert item_item().apply_discount() is None


if __name__ == '__main__':
    pytest.main()

#
# # пример класса для тестирования
# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def sum(self):
#         return self.a + self.b
#
#
# # создание fixture для создания экземпляра класса в каждом тесте
# @pytest.fixture
# def my_class():
#     return MyClass(2, 3)
#
#
# # тест функции sum класса MyClass
# def test_sum(my_class):
#     assert my_class.sum() == 5
