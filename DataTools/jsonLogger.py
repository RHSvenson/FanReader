# Denne funktion kaldes når brugeren har sagt ja til at gemme historik.
# Den skubber alle midlertidige værdier fra director til json filer på den lokale disk.

# Funktionen skal bruge:
# Historiens navn
# Kapitel nummer
# Primære univers
# VALGFRIT: kapitlets kategorier/tags
# VALGFRIT: kapitlets deltagende karakterer

def jsonLogger(storyName, chapterNumber, universe, tags=None, characterList=None):
    import os
    import json

    universePath = "Data/previousStories/"+universe
    storyPath = universepath + "/"+storyName
    chapterPath = storypath + "/"+"chapter"+str(chapterNumber)

    # Start med at danne mappe hvis denne ikke allerede findes
    if os.path.exists(fullPath) == False:
        if os.path.exists(universePath) == False:
            os.mkdir(universePath)
        if os.path.exists(storyPath) == False:
            os.mkdir(storyPath)
        if os.path.exists(chapterPath) == False:
            os.mkdir(chapterPath)
    
    # Eksporter derefter kapitelkarakterer til kapitlets kendte karakterer.
    # Tilføj hidtil ukendte karakterer til historiens kendte karakterer også.
    if characterList != None:
        with open(os.path.join(chapterPath + "/characters.json"), 'w') as jsonfile:
            json.dump(characterList, jsonfile)
        if os.path.exists(storyPath + "/characters.json"):
            with open(os.path.join(storyPath + "/characters.json"), 'r') as jsonfile:
                # Kontroller om nogle af kapitlets karakterer mangler i historiens kendte karakterer.
                knownCharacters = json.load(jsonfile)
                characterIsKnown = False
                for newCharacter in characterList:
                    for character in knownCharacters:
                        if character["Names"] == newCharacter:
                            characterIsKnown = True
                            break
                    # Hvis der ikke er nogen match, tilføj dem til listen.
                    if characterIsKnown == False:
                        newCharacterEntry = {
                            "Names": newCharacter,
                            "Addresses": "Unknown",
                            "Gender": "Unknown",
                            "NarrationType": "Normal"
                        }
                        knownCharacters[newCharacter] = newCharacterEntry
                        with open(os.path.join(storypath + "/character.json"), "w") as newjson:
                            json.dump(knownCharacters, newjson)
                        # Og genindlæs derefter knownCharacters
                        knownCharacters = json.load(os.path.join(storyPath + "/characters.json"))
                        
                        
