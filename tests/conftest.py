import pytest
from src.item import Item


@pytest.fixture
def item_smartphone_10000_20():
    """
    Товар с параметрами:
    name='Смартфон', price=10000, quantity=20
    """
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item_notebook_20000_5():
    """
    Товар с параметрами:
    name='Ноутбук', price=20000, quantity=5
    """
    return Item("Ноутбук", 20000, 5)


@pytest.fixture
def item_notebook_aser_minus_25000_minus_15():
    """
    Товар с параметрами:
    name='Ноутбук_ASER', price=-25000, quantity=-15
    """
    return Item("Ноутбук_ASER", -25000, -15)


@pytest.fixture
def item_notebook_lenovo_0_0():
    """
    Товар с параметрами:
    name='Ноутбук_lenovo', price=0, quantity=0
    """
    return Item("Ноутбук_lenovo", 0, 0)


@pytest.fixture
def test_all_items():
    """
    Список из двух товаров
    """
    return [item_smartphone_10000_20, item_notebook_20000_5]


@pytest.fixture
def pay_rate_1():
    """ Новый уровень цен равен 0.8 """
    return 0.8
