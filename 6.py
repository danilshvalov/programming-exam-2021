def split_values(*args):
    negative = []
    non_negative = []
    for val in args:
        if val < 0:
            negative.append(val)
        else:
            non_negative.append(val)

    negative.sort(reverse=True)
    non_negative.sort()

    return negative, non_negative
