# Funktioner der rengører diverse datastykker

# Ekstraherer characters fra en tag fil.
def charTagsGen(file):
    from re import findall
    with open (file) as tags:
        tags = tags.read()
        # Brug regex til at finde alle tags der er karakterer.
        chartags = re.findall("(?<=Character=\")[\w\d\s]+(?=\")", tags)
        return charTags