# Task 0.9

def find_vowels():

    string = input("Enter word ").lower()
    vowels = "aeiou"
    new_string = ""
    for vowl in string:
        if vowl in vowels:
            new_string = new_string + vowl

    output = ""
    for char in new_string:
        if char not in output:
            output = output + char
            print(char, end=",")


find_vowels()