# Funktion anvendt til at kontrollere tilstedeværelsen af
# sætninger som "I said" omkring en snippet
import sys


def saidChecker(snippet, dictionary, charTags):
    import re
    breakFlag = False
    with open(dictionary) as file:
        synonyms = file.read()
        saidSynonyms = re.findall(pattern="\w+",string=synonyms)
    for synonym in saidSynonyms:
        for character in charTags:
            if breakFlag == True:
                break
            if re.search(character+" "+synonym, snippet[1]) != None:
                phraseCache = (None, snippet[1], ("saidafter", character))
                breakFlag = True
                break
            elif re.search(synonym+" "+character, snippet[1]) != None:
                phraseCache = (None, snippet[1], ("saidafter", character))
                breakFlag = True
                break
            elif re.search("I "+synonym, snippet[1]) != None and snippet[0] == 0:
                phraseCache = (None, snippet[1], ("saidafter", "main"))
                breakFlag = True
                break
            elif re.search("( he )|( He )"+synonym, snippet[1]) != None and snippet[0] == 0:
                phraseCache = (None, snippet[1], ("saidafter", "lastmale"))
                breakFlag = True
                break
            elif re.search("( she )|( She )"+synonym, snippet[1]) != None and snippet[0] == 0:
                phraseCache = (None, snippet[1], ("saidafter", "lastfemale"))
                breakFlag = True
                break
            else:
                phraseCache = (None, snippet[1], None)
            if breakFlag == True:
                break
        return phraseCache
        if breakFlag == True:
            break