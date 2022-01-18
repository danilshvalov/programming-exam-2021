def clear_array(array):
    result = []
    for val in array:
        if val is not None:
            result.append(val)
    return result


array = [1, 2, None, 4, None, 6]

result1 = clear_array(array)  # 1-й способ
result2 = list(filter(lambda x: x is not None, array))  # 2-й способ

assert result1 == result2  # проверка эквивалентности способов

print(result1)
