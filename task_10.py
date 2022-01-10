# Task 0.10

def common_char(string1, string2):

    common = ""
    for char in string1:
        if char in string2:
            common = common + char

    output = ""
    for i in common:
        if i not in output:
            output = output + i
    print(*output, sep=",")


common_char("computers", "house")