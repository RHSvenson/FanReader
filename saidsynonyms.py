import re

def synonyms(arg):
    saidSynonyms = "[(said)(spoke)(aired)(shared)(sounded)(vented)(voiced)(blabbered)(blurted)(announced)(broadcast)(declared)(proclaimed)(affirmed)(alleged)(asserted)(breathed)(chirped)(gasped)(mouthed)(purred)(shouted)(spluttered)(spouted)(whispered)(commented)(remarked)]"
    if arg == "said":
        return saidSynonyms

def charTagsGen(file):
    from re import findall
    with open (file) as tags:
        tags = tags.read()
        # Find alle tags markeret som karakterer
        # Dette kræver et specifikt layout i listen. Vi har ingen API access endnu, så det er svært at forudsige hvordan denne reelt vil se ud.
        charTags = re.findall("(?<=Character=\")[\w\d\s]+(?=\")", tags)
        return charTags

def saidChecker(snippets):
    from re import search
    saidSynonyms = synonyms("said")
    charTags = charTagsGen("exampletags.txt")
    for analysisObject in snippets:
        for character in charTags:
            if re.search(str(character)+" "+saidSynonyms,analysisObject[1]) != None:
                return character
                break
            elif re.search(saidSynonyms+" "+str(character), analysisObject[1]) != None:
                return character
                break
            elif re.search(saidSynonyms+" "+"I", analysisObject[1]) != None:
                return "Main"
                break
            elif re.search("I"+" "+saidSynonyms, analysisObject[1]) != None:
                return "Main"
                break