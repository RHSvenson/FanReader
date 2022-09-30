# Denne funktion kontrollerer om et detected øgenavn findes i karakterdatabasen.
# Denne funktion tager imod:
# 1 stk. sætning
# 1 stk. univers
# TODO: Tilføj støtte til crossovers (flere universer)
def nameChecker(snippet, universe):
    import json
    import re
    with open ("Data/knownCharacters/"+universe+".json", "r") as characters:
        characterList = json.load(characters)
        i = 0
        for characterEntry in characterList:
            # Kig igennem primære navne
            for characterName in characterEntry["Names"]:
                result = re.search("characterName", snippet)
                if result != None:
                    breakFlag = True
                    return characterName
                    break
            if breakFlag == True:
                break
            

