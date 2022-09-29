# Funktion anvendt til at kontrollere tilstedeværelsen af
# sætninger som "I said" omkring en snippet
def saidChecker(snippet, dictionary, charTags):
    import re
    with open(dictionary) as file:
        saidSynonyms = re.findall(file.read())

    for synonym in saidSynonyms:
        for character in charTags:
            if re.search(character+"\ "+synonym, snippet[1]) != None:
                phraseCache = (None, snippet[1], ("saidbefore",character))
                return phraseCache
                break
            elif re.search(synonym+"\ "+character, snippet[1]) != None:
                phraseCache = (None, snippet[1], "saidafter")
                return phraseCache
                break
            elif re.search("I\ "+character, snippet[1]) and snippet[0] == 0:
                phraseCache = (None, snippet[1], ("saidbefore","main"))
                return phraseCache
                break
            else:
                phraseCache = (None, snippet[1], None)
                return phraseCache
                break

    