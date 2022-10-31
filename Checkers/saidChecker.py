# Funktion anvendt til at kontrollere tilstedeværelsen af
# sætninger som "I said" omkring en snippet
import sys


def saidChecker(snippet, dictionary, charTags):
    import re
    breakFlag = False
    with open(dictionary) as file:
        synonyms = file.read()
        saidSynonyms = re.findall(pattern="\w+",string=synonyms)
    phraseCache = {
        "Character": None,
        "Sentence": snippet[1],
        "Parameters": (None, None)
    }
    # Start af loopsekvense. Disse leder tilsammen igennem alle navne og synonymer.
    for synonym in saidSynonyms:
        for characterEntry in charTags:
            for characterName in charTags[characterEntry]["Names"]:
                # Slutning af loopsekvens.
                if breakFlag == True:
                    break
                if re.search(characterName+" "+synonym, snippet[1]) != None:
                    phraseCache = {
                        "Parameters": ("characterafter", characterName)
                    }
                    breakFlag = True
                    break
                elif re.search(synonym+" "+characterName, snippet[1]) != None:
                    phraseCache = {
                        "Parameters": ("characterafter", characterName)
                    }
                    breakFlag = True
                    break
                elif re.search("I "+synonym, snippet[1]) != None and snippet[0] == 0:
                    phraseCache = {
                        "Parameters": ("characterafter", "main")
                    }
                    breakFlag = True
                    break
                elif re.search("( he )|( He )"+synonym, snippet[1]) != None and snippet[0] == 0:
                    phraseCache = {
                        "Parameters": ("characterafter", "lastmale")
                    }
                    breakFlag = True
                    break
                elif re.search("( she )|( She )"+synonym, snippet[1]) != None and snippet[0] == 0:
                    phraseCache = {
                        "Parameters": ("pronounafter", "lastfemale")
                    }
                    breakFlag = True
                    break
                # Last resort, indikerer at vi har et synonym match men ingen karakter.
                # Bruges af director til at kalde på addresschecker.
                elif re.search(synonym, snippet[1]) != None and snippet[0] == 0:
                    phraseCache = {
                        "Parameters": ("addressafter", None)
                    }
                else:
                    phraseCache = {
                        "Character": None, 
                        "Sentence": snippet[1],
                        "Parameters": None
                    }
                if breakFlag == True:
                    break


        return phraseCache
        if breakFlag == True:
            break