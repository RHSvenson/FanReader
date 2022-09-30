# Denne funktion kaldes når brugeren har sagt ja til at gemme historik.
# Den skubber alle midlertidige værdier fra director til json filer på den lokale disk.

# Funktionen skal bruge:
# Historiens navn
# Kapitel nummer
# Primære univers
# VALGFRIT: kapitlets kategorier/tags
# VALGFRIT: kapitlets deltagende karakterer

def jsonLogger(storyName, chapterNumber, universe, tags=None, characterList=None):
    