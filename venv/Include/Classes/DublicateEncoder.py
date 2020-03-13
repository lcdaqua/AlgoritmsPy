def duplicate_encode(word):

    symbols = list(word.lower())
    result = ""

    for i in range (0, len(symbols)):

        counter = 0

        for j in range (0, len(symbols)):

            if symbols[i] == symbols[j]:

                counter += 1

        if counter > 1:
            result += ")"
        else:
            result += "("

    return result