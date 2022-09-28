# Funktion anvendt til at kontrollere tilstedeværelsen af
# sætninger som "I said" omkring en snippet
def saidChecker(snippets, dictionaryPath, charTags):
    import re
    with open(dictionaryPath) as file:
        saidSynonyms = file.read()
    for analysisObject in snippets:
        for character in charTags:
            if re.search(character+" "+saidSynonyms,analysisObject[1]) != None:
                return character
                break
            elif re.search(saidSynonyms+" "+character, analysisObject[1]) != None:
                return character
                break
            elif re.search(saidSynonyms+"\ I", analysisObject[1]) != None:
                return "Main"
                break
            elif re.search("I\ "+saidSynonyms, analysisObject[1]) != None:
                return "MainX"
                break
            else:
                return "F"
                break