def pig_it(text):
    words = text.split(" ")
    for i in range (0, len(words)):
        if words[i] != "!" and words[i] != "?" and words[i] != "." and words[i] != ",":
            firstLetter = words[i][:1]
            words[i] = words[i][1:len(words[i])] + firstLetter + "ay"

    result = " ".join(words)
    return result