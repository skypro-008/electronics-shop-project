import src.item as my_item

if __name__ == '__main__':
    item1 = my_item.Item("Смартфон", 10000, 20)
    item2 = my_item.Item("Ноутбук", 20000, 5)

    #  1 вариант
    # print(item1.calculate_total_price())  # 200000
    # print(item2.calculate_total_price())  # 100000
    #  2 вариант
    print(*[item.calculate_total_price() for item in my_item.Item.all],
          sep='\n')

    # устанавливаем новый уровень цен
    my_item.Item.pay_rate = 0.8
    # применяем скидку на первый товар
    item1.apply_discount()

    #  1 вариант
    # print(item1.price)  # 8000.0
    # print(item2.price)  # 20000
    #  2 вариант
    print(*[item.price for item in my_item.Item.all], sep='\n')

    print(my_item.Item.all)

    #мой вывод
    print()
    for item in my_item.Item.all:
        print(f'{item.name} в количестве {item.quantity} '
              f'по цене {my_item.nice_number_output(item.price)} руб. '
              f'Итоговая сумма = '
              f'{my_item.nice_number_output(item.calculate_total_price())} '
              f' руб.')

