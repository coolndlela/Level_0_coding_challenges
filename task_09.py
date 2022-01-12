
def find_vowels(string):
    string = string.lower()

    vowels = "aeiou"
    new_string = ""
    for vowl in string:
        if vowl in vowels:
            new_string = new_string + vowl

    output = ""
    for char in new_string:
        if char not in output:
            output = output + char

    print ("Vowels: ", end="")
    print (*output, sep=",")


find_vowels("Umuzi")
