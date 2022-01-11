
def calc_triangle_area(num1, num2, num3):
    semi_perimeter = (num1 + num2 + num3) / 2
    area = (semi_perimeter*((semi_perimeter-num1)*(semi_perimeter-num2)*(semi_perimeter-num3))) ** 0.5
    return area


calc_triangle_area(21, 10, 13)