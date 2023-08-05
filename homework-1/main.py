import src.item as my_item

if __name__ == '__main__':
    item1 = my_item.Item("Смартфон", 10000, 20)
    item2 = my_item.Item("Ноутбук", 20000, 5)

    # print(item1.calculate_total_price())  # 200000
    # print(item2.calculate_total_price())  # 100000
    print(*[item.calculate_total_price() for item in my_item.Item.all], sep='\n')

    # устанавливаем новый уровень цен
    my_item.Item.pay_rate = 0.8
    # применяем скидку на первый товар
    item1.apply_discount()

    # print(item1.price)  # 8000.0
    # print(item2.price)  # 20000
    print(*[item.price for item in my_item.Item.all], sep='\n')

    print(my_item.Item.all)  # [<__main__.Item object at 0x000001EC6250C690>, <__main__.Item object at 0x000001EC6250C6D0>]

    #мой вывод
    print()
    for item in my_item.Item.all:
        print(f'{item.name} в количестве {item.quantity} по цене {my_item.nice_number_output(item.price)} руб. '
              f'Итоговая сумма = {my_item.nice_number_output(item.calculate_total_price())} руб.')
    # print(f'{item2.name} в количестве {item2.quantity} по цене {my_item.nice_number_output(item2.price)} руб. '
    #       f'Итоговая сумма = {my_item.nice_number_output(item2.calculate_total_price())} руб.')
