# Denne kontrollerer hvem der var hovedfokus i sidste stykke narration
# Den er ubrugelig alene, men kan samarbejde med f.eks. exchangeChecker som last-resort

def endFocusChecker(loadedPhrase=phraseCache, charTags=charTags):
    import re
    for characterEntry in charTags:
        if breakFlag == True:
            break
        for charaterName in charTags[characterEntry]["Names"]:
            # Loop igennem alle navne, og kontroller om de er tilstede i snippeten
            if breakFlag == True:
                break

            # Kontroller om karakternavnet er tilstede i sætningen
            elif re.search(characterName, loadedPhrase["Sentence"]) != None:
                phraseCache = {
                    # Kopier den data der ikke skal ændres
                    "Character": loadedPhrase["Character"],
                    "Sentence": loadedPhrase["Sentence"],
                    # Og indsæt et parameter for at indikere den fundne karakter
                    "Parameters": ("endfocus", characterName)
                }

            # Ellers så giv bare phrasen tilbage uændret
            else:
                phraseCache = loadedPhrase
    
    return phraseCache