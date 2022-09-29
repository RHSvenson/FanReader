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
            if re.search(character+"\ "+synonym, snippet[1]) != None:
                phraseCache = (None, snippet[1], ("saidbefore",character))
                return phraseCache
                breakFlag = True
                break
            elif re.search(synonym+"\ "+character, snippet[1]) != None:
                phraseCache = (None, snippet[1], "saidafter")
                return phraseCache
                breakFlag = True
                break
            elif re.search("I\ "+character, snippet[1]) and snippet[0] == 0:
                phraseCache = (None, snippet[1], ("saidbefore","main"))
                return phraseCache
                breakFlag = True
                break
            else:
                phraseCache = (None, snippet[1], None)
                return phraseCache
                breakFlag = True
                break
            if breakFlag == True:
                break
        if breakFlag == True:
            break
    