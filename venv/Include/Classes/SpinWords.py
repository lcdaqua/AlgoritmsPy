def spin_words(sentence):
    splitWords = sentence.split()
    newSentence = []
    finalSentence = ""

    for i in range (0, len(splitWords)):
        if len(splitWords[i]) >= 5:
            newSentence.append(splitWords[i][::-1])
            finalSentence += newSentence.pop() + " "

        else:
            newSentence.append(splitWords[i])
            finalSentence += newSentence.pop() + " "

    return finalSentence.strip()