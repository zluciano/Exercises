def cleanword(word):
    newWord = ""
    for i in word:
        if(i.isalpha()):
            newWord += i
    return newWord

def has_dashdash(word):
    if "--" in word:
        return True
    else:
        return False

def extract_words(text):
    newText = []
    c = ""
    for x in text:
        if x.isalpha() and x != text[-1]:
            c += x
        elif x.isalpha():
            c += x
            newText.append(c)
            c = ""
        elif c != "":
            newText.append(c)
            c = ""
    return [y.lower() for y in newText]


def wordcount(word, list):
    n = 0
    for words in list:
        if words == word:
            n += 1
    return n

def wordset(text):
    chosen = []
    newText = []
    for word in text:
        if word not in chosen:
            newText.append(word)
            chosen.append(word)
    return sorted(newText)

def longestword(text):
    greater = 0
    for word in text:
        if greater < len(word):
            greater = len(word)
    return greater