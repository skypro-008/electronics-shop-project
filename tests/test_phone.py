import pytest


@pytest.mark.parametrize('name, price, quantity, number_of_sim, expected_result', [
    ('IPhone', 100_000, 3, 1, "Phone('IPhone', 100000, 3, 1)"),
    ('Samsung', 50_000, 6, 2, "Phone('Samsung', 50000, 6, 2)"),
    ('Xiaomi', 40_000, 8, 2, "Phone('Xiaomi', 40000, 8, 2)"),
])
def test_repr(phone, name, price, quantity, number_of_sim, expected_result):

    phone.name = name
    phone.price = price
    phone.quantity = quantity
    phone.number_of_sim = number_of_sim

    assert repr(phone) == expected_result


@pytest.mark.parametrize('name, expected_result', [
    ('Sony', 'Sony'),
    ('OnePlus', 'OnePlus'),
    ('LG', 'LG'),
])
def test_str(phone, name, expected_result):

    phone.name = name
    assert str(phone) == expected_result


@pytest.mark.parametrize('number_of_sim, expected_result', [
    (1, 1),
    (2, 2),
])
def test_number_of_sim_valid(phone, number_of_sim, expected_result):

    phone.number_of_sim = number_of_sim
    assert phone.number_of_sim == expected_result


@pytest.mark.parametrize('number_of_sim', [
    (0, ),
    (3, ),
])
def test_number_of_sim_invalid(phone, number_of_sim):

    with pytest.raises(ValueError):
        phone.number_of_sim = number_of_sim
