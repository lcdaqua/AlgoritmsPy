def order(sentence):

  splitWords = sentence.split()
  newSentence = []
  finalSentence = ""

  for i in range (1, len(splitWords)+1):
      for k in range (0, len(splitWords)):
          if str(i) in splitWords[k]:
              finalSentence += splitWords[k] + " "

  return finalSentence.strip()