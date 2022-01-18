def combine_numbers(first, second):
    if first > second:
        return first - second
    if first < second:
        return first + second
    return first


first, second = map(int, input().split())
third = combine_numbers(first, second)
print(third)
