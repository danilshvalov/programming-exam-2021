def add_extra_charge(val):
    return val * 1.2


def update_price(cost):
    result = []
    for val in cost:
        result.append(add_extra_charge(val))

    return result


cost = [1, 20, 3, 10, 5, 7, 2, 4, 9, 8]
price1 = update_price(cost)  # 1-й способ
price2 = list(map(add_extra_charge, cost))  # 2-й способ

assert price1 == price2  # проверка эквивалентности способов

print(price1)
