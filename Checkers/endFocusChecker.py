# Denne kontrollerer hvem der var hovedfokus i sidste stykke narration
# Bemærk at dette er en fallback funktion, da den er upålidelig i dens nuværende tilstand.

def endFocusChecker(snippet, charTags):
    import re
    for character in charTags:
        if re.search(str(character)+"(?=( [A-Za-z]+){0,5}\.)", snippet) != None:
            return str(character)
            break