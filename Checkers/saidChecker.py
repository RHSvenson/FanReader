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
                phraseCache = {
                    "Character": None,
                    "Sentence": snippet[1],
                    "Parameters": ("saidafter", character)
                }
                breakFlag = True
                break
            elif re.search(synonym+" "+character, snippet[1]) != None:
                phraseCache = {
                    "Character": None,
                    "Sentence": snippet[1],
                    "Parameters": ("saidafter", character)
                }
                breakFlag = True
                break
            elif re.search("I "+synonym, snippet[1]) != None and snippet[0] == 0:
                phraseCache = {
                    "Character": None,
                    "Sentence": snippet[1],
                    "Parameters": ("saidafter", "main")
                }
                breakFlag = True
                break
            elif re.search("( he )|( He )"+synonym, snippet[1]) != None and snippet[0] == 0:
                phraseCache = {
                    "Character": None, 
                    "Sentence": snippet[1], 
                    "Parameters": ("saidafter", "lastmale")
                }
                breakFlag = True
                break
            elif re.search("( she )|( She )"+synonym, snippet[1]) != None and snippet[0] == 0:
                phraseCache = {
                    "Character": None,
                    "Sentence": snippet[1],
                    "Parameters": ("saidafter", "lastfemale")
                }
                breakFlag = True
                break
            else:
                phraseCache = {
                    "Character": None, 
                    "Sentence": snippet[1],
                    "Parameters": None
                }
            if breakFlag == True:
                break

        # Hvis der ikke findes nogen matches fra det første loop, så begyn at kigge på aliases
        for addresses in 


        return phraseCache
        if breakFlag == True:
            break