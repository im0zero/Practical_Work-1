def find_second_max():
    num = int(input())

    if num == 0:
        return 0, 0

    first, second = find_second_max()

    if first == 0:
        return num, 0

    if num > first:
        return num, first
    elif num > second or second == 0:
        return first, num
    else:
        return first, second


first_max, second_max = find_second_max()
print(second_max)