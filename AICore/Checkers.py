# Alle funktioner der analyserer sprogbrug er i denne fil.

# Denne funktion kontrollerer den angivne liste string for
# sætninger såsom "I said". Disse giver en høj sandsynlighed.
def saidChecker(snippets):
    from re import search
    import FanReader.Cleaners.MiscCleaners
    import os

    # Påkrævet for at finde vores tekst filer
    currentPath = os.path.dirname(__file__)
    dictionaryPath = os.path.join(currentPath, "../Dictionaries/SaidSynonyms.txt")
    charTagsPath = os.path.join(currentPath, "../exampletags.txt")

    # Indlæsning af dictionary og karakter tags.
    dictionary = open(dictionaryPath).read()
    characterTags = charTagsGen(charTagsPath)

    print(characterTags)

saidChecker("Hey")