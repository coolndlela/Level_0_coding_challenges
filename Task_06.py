# Task 0.6
def get_max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(get_max_num(1, 4, 12))


# upgrading the above function any amount of numbers
def get_max_num(*numbers):
    max_num = numbers[0]
    for i in numbers:
        if i >= max_num:
            max_num = i

    return max_num


print(get_max_num(1, 22, 3, 2))