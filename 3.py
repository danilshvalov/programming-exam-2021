def align_value(val):
    if val < 10:
        return val * 1.13
    if val > 10:
        return val * 0.18
    return val


def align_array(array):
    result = []
    for val in array:
        result.append(align_value(val))

    return result


array = [1, 20, 3, 10, 5]
result1 = align_array(array)  # 1-й способ
result2 = list(map(align_value, array))  # 2-й способ

assert result1 == result2  # проверка эквивалентности способов

print(result1)
print(array)
