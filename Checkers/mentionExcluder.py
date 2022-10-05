# Denne checker udelukker en karakter nævnt i en sætning fra at eje sætningen.
# Bemærk at denne kun skal kaldes hvis karakteren har normal udtryk.
# Altså skal den udelukkes for karakterer der taler i f.eks. tredjeperson.

def mentionExcluder(snippet, charTags):
    import re

    for character in charTags:
        if re.search(character, snippet) != None:
            return True
        else:
            return False