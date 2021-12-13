# Task 0.7
# converts Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


print(celsius_to_fahrenheit(33))


# Converts Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(celsius)


fahrenheit_to_celsius(91.4)