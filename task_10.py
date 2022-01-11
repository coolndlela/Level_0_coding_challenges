
def common_char(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    common = ""

    for char in string1:
        if char in string2:
            common = common + char

    output = ""
    for i in common:
        if i not in output:
            output = output + i
    print(*output, sep=", ")


common_char("computers", "house")