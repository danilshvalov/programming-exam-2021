def reverse_number(number):
    result = 0
    sign = 1
    if number < 0:
        sign = -1

    number *= sign

    while number != 0:
        result = result * 10 + number % 10
        number //= 10

    return result * sign


number = int(input())
result = reverse_number(number)
print(result)
