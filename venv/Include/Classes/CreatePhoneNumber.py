def create_phone_number(n):
    code = str(n[0]) + str(n[1]) + str(n[2])
    firstPart = str(n[3]) + str(n[4]) + str(n[5])
    secondPart = str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
    result = "(" + code + ") " + firstPart + "-" + secondPart
    return result

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)