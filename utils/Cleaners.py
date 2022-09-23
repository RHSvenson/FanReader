# Funktioner til oprensning af data.

# Filtering af karakter tags.

def charTagsGen(file):
    with open (file) as tags:
        tags = tags.read()
        # Find alle tags markeret som karakterer
        # Dette kræver et specifikt layout i listen. Vi har ingen API access endnu, så det er svært at forudsige hvordan denne reelt vil se ud.
        import re
        charTags = re.findall("(?<=Character=\")[\w\d\s]+(?=\")", tags)
        return charTags