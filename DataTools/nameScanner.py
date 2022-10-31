# Denne funktion kontrollerer tilstedeværende karakterer i kapitlet
# Derudover kan den også se efter ukendte karaktere ved at scanne efter øgenavne.

# Denne funktion tager imod:
# 1 stk. snippetlist
# 1 stk. univers
# Valgfrie argumenter
# TODO: Tilføj støtte til crossovers (flere universer)
def nameScanner(snippetList="snippetList", universe="", args="fullScan"):
    import json
    import re

    with open("Data/knownCharacters/"+universe+".json", "r") as file:
        universecharDict = json.load(file)

    charDict = {}
    
    # Som udgangspunkt udfører programmet altid et fuldt scan.
    # Dette indebærer at den kontrollerer om hver eneste karakter er til stede.
    # TODO: Gør dette valgfrit, med muligheder for tag-baseret, eller tidligere kapitel baseret.
    if "fullScan" in args:
        for entry in universecharDict:
            breakFlag = False
            # Kig igennem karakterenes navneliste
            for name in universecharDict[entry]["Names"]:
                if breakFlag == True:
                    break
                # Og sammenlign den med snippets indhold for at som vi har et match.
                for snippet in snippetList:
                    if breakFlag == True:
                        break
                    elif re.search(name, snippet[1]) != None:
                        charDict[entry] = universecharDict[entry]
                        breakFlag = True

    # Hvis det ikke er angivet, så kigger vi bagefter igennem alle snippets en efter en
    # for at kigge efter øgenavne. Dette kræver meget brugeinput, og burde derfor nok
    # advares om inden man trykker start.
    breakFlag = False
    repeatList = []
    counter = 0
    if "noNewNames" not in args:
        for snippet in snippetList:
            breakFlag = False
            counter = counter+1
            resultList = re.findall(r"(?<=[a-z]|[A-Z|\"|\,])(?: )(([A-Z][a-z]{1,15} ?){1,5})", snippet[1])
            if resultList != []:
                for x in resultList:
                    # overfør resultatet fra tuple konstrukt fra re.findall
                    result = x[0]
                    # Fjerne overskydende mellemrum for enden og i starten af string
                    if result[0] == " ":
                        result = result[1:]
                    if result[-1] == " ":
                        result = result[:-1]
                    # Afbryd hvis vi kender navnet i forvejen.
                    for entry in charDict:
                        if breakFlag == True:
                            break
                        # Scanner efter kendte navne i det overordnede dictionary
                        for name in charDict[entry]["Names"]:
                            if re.search(name, result) != None:
                                breakFlag = True
                                break
                        # Scanner efter ord som vi allerede har sagt nej til før.
                        for repeat in repeatList:
                            if re.search(repeat, result) != None:
                                breakFlag = True
                                break
                    if breakFlag == True:
                        break
                    # Kontroller efter gyldigt input
                    # TODO: Erstat denne med gui responser
                    print("Ukendt øgenavn fundet: \""+str(result)+"\" i linje "+str(counter))
                    print("Skal denne gemmes? (J/N):")
                    saveResponse = str(input())
                    while re.search("j|J|n|N", saveResponse) == None:
                        print("Ugyldigt input, angiv J eller N:")
                        saveResponse = str(input())

                    # Loop til ja eller nej slut
                    if re.search("j|J", saveResponse) != None:
                        # Findes karakteren allerede?
                        print("Er dette en titel til en eksisterende karakter? (J/N):")
                        existingResponse = str(input())

                        # Loop til at fange forkerte input.
                        while re.search("j|J|n|N", saveResponse) == None:
                            print("Ugyldigt input, angiv J eller N:")
                            existingResponse = str(input())
                        if re.search("j|J", existingResponse) != None:
                            breakFlag = False
                            firstLoop = True
                            for entry in charDict:
                                print(entry)
                            print("Indtast venligst en af ovenstående karakterer som titlen passer til.")
                            while breakFlag == False:
                                if firstLoop == False:
                                    print("Ugyldigt input, prøv igen.")
                                userInput = str(input())
                                for entry in charDict:
                                    if entry.lower == userInput.lower:
                                        charDict[entry]["Addresses"].append(result)
                                        breakFlag = True
                                        print("Title added.")
                                        break
                                firstLoop = False
                                
                            
                        elif re.search("n|N", existingResponse) != None:
                            charDict[result] = newCharEntry(result)
                    else:
                        # Tilføj entry til en liste over ting som ikke skal spørges om igen.
                        repeatList.append(result)


                        




    print(charDict)
    return charDict

def newCharEntry(Names):
    import re
    print("Er karakteren en mand eller kvinde? (M/K):")
    genderResponse = str(input())
    while re.search("m|M|k|K", genderResponse) == None:
        print("Ugyldigt input, angiv m eller k:")
        genderResponse = str(input())
    if re.search("m|M", genderResponse) != None:
        genderResponse = "Male"
    elif re.search("k|K", genderResponse) != None:
        genderResponse = "Female"
    # Nu har vi alt hvad vi skal bruge indtil videre, så vi føjer det hele
    # til charDict.
    
    newEntry = {
        "Names": [Names],
        "Addresses": [],
        "Gender": genderResponse,
        "NarrationType": "Normal"
    }
    return newEntry