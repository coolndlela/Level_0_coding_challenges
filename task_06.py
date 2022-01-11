# Task 0.6

def get_max_num(*numbers):
    max_num = numbers[0]
    for i in numbers:
        if i >= max_num:
            max_num = i

    return max_num


print(get_max_num(1, 3, 2, 4, 10))