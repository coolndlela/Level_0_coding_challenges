# Task 0.5
from math import sqrt


def calc_triangle_area(num1, num2, num3):
    semi_perimeter = (num1 + num2 + num3) / 2
    area = sqrt(semi_perimeter*((semi_perimeter-num1)*(semi_perimeter-num2)*(semi_perimeter-num3)))
    return area

