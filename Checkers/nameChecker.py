# Denne funktion kontrollerer tilstedeværende karakterer i kapitlet
# Derudover kan den også se efter ukendte karaktere ved at scanne efter øgenavne.
# Dette kan slås fra ved at passe args="NoNewNames"

# Denne funktion tager imod:
# 1 stk. snippetlist
# 1 stk. univers
# Valgfrie argumenter
# TODO: Tilføj støtte til crossovers (flere universer)
def nameChecker(snippetList, universe, args=""):
    import json
    import re
    chapterActors = []
    breakFlag = False
    with open ("Data/knownCharacters/"+universe+".json", "r") as characters:
        characterList = json.load(characters)
        for snippet in snippetList:
            # Brug JSON databasen til at scanne igennem kendte navne
            for characterEntry, characterInfo in characterList.items():
                # Kig igennem primære navne
                for characterName in characterInfo["Names"]:
                    result = re.search(characterName, snippet[1])
                    if result != None:
                        breakFlag = True
                        print(characterEntry)
                        chapterActors.append(characterEntry)
                        break
                if breakFlag == True:
                    break
                # Hvis der ikke blev fundet noget, så tjek lige efter typiske øgenavnsindikatorer.
                # Dette kan slås fra, da den kan give mange returns grundet stednavne.
            if "NoNewNames" not in args:
                result = re.findall("(?<= )([A-Z][a-z]+ ?){1,5}", snippet[1])
                print(result)
                # Spørg brugeren om navnet kan passe
                if result != None:
                    print("Ukendt øgenavn: "+result)
                    print("Skal denne gemmes som en ny karakter? (J/N):")
                    breakFlag = False
                    while breakFlag == False:
                        userInput = str(input())
                        if userInput == "J":
                            # Gem karakteren i karakterlisten
                            chapterActors.append(result)
                            print("Navn gemt.")
                            breakflag = True
                        elif userInput == "N":
                            print("Navn glemt")
                            breakFlag = True
                        else:
                            print("Ugyldigt input.")

            breakFlag = False
    return chapterActors
            

