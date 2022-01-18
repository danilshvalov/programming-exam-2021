def iterative_pow(number, power):
    assert power >= 0  # проверяем, что степень не отрицательна

    result = 1
    while power > 0:
        result *= number
        power -= 1

    return result


def recursive_pow(number, power):
    assert power >= 0  # проверяем, что степень не отрицательна

    if power == 0:
        return 1

    return number * recursive_pow(number, power - 1)


assert iterative_pow(2, 0) == 1
assert iterative_pow(2, 1) == 2
assert iterative_pow(2, 2) == 4
assert iterative_pow(2, 3) == 8

assert recursive_pow(2, 0) == iterative_pow(2, 0)
assert recursive_pow(2, 1) == iterative_pow(2, 1)
assert recursive_pow(2, 2) == iterative_pow(2, 2)
assert recursive_pow(2, 3) == iterative_pow(2, 3)
