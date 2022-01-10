# Task 0.6
def get_max_num(num1, num2, num3):
    numbers = (num1, num2, num3)
    max_num = numbers[0]

    for i in numbers:
        if i > max_num:
            max_num = i

    return max_num


get_max_num(66, 4, 12)


def get_max_num(*numbers):
    max_num = numbers[0]
    for i in numbers:
        if i >= max_num:
            max_num = i

    return max_num


get_max_num(1, 22, 3, 2)